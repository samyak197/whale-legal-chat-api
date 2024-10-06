from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import google.generativeai as genai
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import silhouette_score
from transformers import AutoTokenizer, AutoModel
import torch

# Google Gemini API key
gemini_api_key = "AIzaSyCuFlDA-DbJjBS6o1Ej-rIbKf4ixjzfndw"
genai.configure(api_key=gemini_api_key)
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
max_chunk_size = 100
max_seq_length = 2048
dtype = (
    None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
)
load_in_4bit = True  # Use 4bit quantization to reduce memory usage
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)


class AIChatbot:
    def __init__(self):
        # Load the main language model
        # self.model, self.tokenizer = FastLanguageModel.from_pretrained(
        #     model_name="unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit",
        #     max_seq_length=max_seq_length,
        #     dtype=dtype,
        #     load_in_4bit=load_in_4bit,
        # )

        # # Enable native 2x faster inference
        # FastLanguageModel.for_inference(self.model)

        # Load the embedding model for semantic chunking
        self.max_chunk_size = 100
        self.max_seq_length = 2048
        self.dtype = None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
        self.load_in_4bit = True
        self.embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
        self.embedding_tokenizer = AutoTokenizer.from_pretrained(
            self.embedding_model_name
        )
        self.embedding_model = AutoModel.from_pretrained(self.embedding_model_name)

        # Load and process the input text

        self.file_path = "legaldoc.txt"
        self.chunked_texts, self.embeddings, self.chunks = self.process_text(
            self.file_path
        )
        self.gemini_api_key = "AIzaSyCuFlDA-DbJjBS6o1Ej-rIbKf4ixjzfndw"
        genai.configure(api_key=self.gemini_api_key)
        self.embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"

    def encode_text(self, text):
        """Encode text into embeddings using a pre-trained model."""
        inputs = self.embedding_tokenizer(
            text, return_tensors="pt", truncation=True, padding=True
        )
        with torch.no_grad():
            outputs = self.embedding_model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).numpy()
        return embeddings

    def chunk_text(self, text):
        """Chunk the text into smaller pieces."""
        tokens = self.embedding_tokenizer.tokenize(text)
        token_chunks = [
            tokens[i : i + self.max_chunk_size]
            for i in range(0, len(tokens), self.max_chunk_size)
        ]
        text_chunks = [
            self.embedding_tokenizer.convert_tokens_to_string(chunk)
            for chunk in token_chunks
        ]
        return text_chunks

    def determine_optimal_clusters(self, embeddings, max_clusters=10):
        """Determine the optimal number of clusters using the Elbow Method and Silhouette Score."""
        distortions = []
        silhouette_scores = []
        K = range(2, max_clusters + 1)

        for k in K:
            kmeans = KMeans(n_clusters=k, n_init=10, random_state=0)
            kmeans.fit(embeddings)
            labels = kmeans.labels_
            distortions.append(kmeans.inertia_)
            if k > 1:
                silhouette_scores.append(silhouette_score(embeddings, labels))

        if silhouette_scores:
            optimal_clusters = K[1:][np.argmax(silhouette_scores)]
        else:
            optimal_clusters = K[0]

        return optimal_clusters

    def semantic_chunking(self, text):
        """Perform semantic chunking on the text using dynamic clustering."""
        chunks = self.chunk_text(text)
        embeddings = np.vstack([self.encode_text(chunk) for chunk in chunks])

        # Determine the optimal number of clusters
        optimal_clusters = self.determine_optimal_clusters(embeddings)

        # Perform KMeans clustering with the optimal number of clusters
        kmeans = KMeans(n_clusters=optimal_clusters, n_init=10, random_state=0)
        kmeans.fit(embeddings)
        labels = kmeans.labels_

        # Group chunks by cluster
        chunked_texts = {i: [] for i in range(optimal_clusters)}
        for i, label in enumerate(labels):
            chunked_texts[label].append(chunks[i])

        return chunked_texts, embeddings, chunks

    def retrieve_chunks(self, query, top_n=5):
        """Retrieve and return the most similar chunks based on a query."""
        query_embedding = self.encode_text(query)

        # Compute cosine similarities
        similarities = cosine_similarity(query_embedding, self.embeddings).flatten()

        # Get indices of the top_n most similar chunks
        top_indices = np.argsort(similarities)[-top_n:][::-1]

        # Retrieve the most similar chunks and join them into a single string
        retrieved_chunks = " ".join(self.chunks[index] for index in top_indices)

        return retrieved_chunks

    def process_text(self, file_path):
        """Read and process the input text from a file."""
        with open(file_path, "r", encoding="utf-8") as file:
            input_text = file.read()

        return self.semantic_chunking(input_text)

    def generate_response(self, question):
        """Generate a response to a given question using Google Gemini."""
        # Retrieve chunks related to the query
        context = self.retrieve_chunks(question)
        # print(context)

        # Define the input template for the Google Gemini API
        input_template = """
            <|begin_of_text|><|start_header_id|>system<|end_header_id|>

            Cutting Knowledge Date: December 2023
            Today Date: 2nd October 2024
            <|eot_id|><|start_header_id|>user<|end_header_id|>

            You are a helpful assistant that responds to the user based on the context provided. You can wish or greet the user. If the answer does not lie in the context, you will respond with 'I don't have sufficient information.'But if it is related to legal docs generation answer their queries.

            Context: {context}
            Question: {question}

            <|eot_id|><|start_header_id|>assistant<|end_header_id|>
        """

        # Format the input text using the context and question
        input_text = input_template.format(context=context, question=question)

        # Generate the response using Google Gemini
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(input_text)

        return response.text


from chat import AIChatbot

chatbot = AIChatbot()


@app.post("/ask/")
async def ask_question(request: Request):
    # Extract question from the request

    request_data = await request.json()
    question = request_data.get("question", "")

    # Stream the response back to the client
    return StreamingResponse(
        chatbot.generate_response(question), media_type="text/plain"
    )
