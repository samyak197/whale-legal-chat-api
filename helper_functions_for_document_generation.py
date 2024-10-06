from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from datetime import datetime


def generate_agreement_of_sale_pdf(
    file_name,
    seller_name,
    seller_father_name,
    seller_age,
    seller_address,
    purchaser_name,
    purchaser_father_name,
    purchaser_age,
    purchaser_address,
    schedule_property,
    sale_amount,
    advance_amount,
    cheque_no,
    bank_name,
    cheque_date,
    balance_amount,
    transaction_end_date,
    purpose_of_sale,
    seller_wife,
    seller_sons_daughters,
    witness_1,
    witness_2,
    previous_owner,
    previous_sale_deed_date,
    previous_sale_doct_no,
    previous_sale_book1_volumne_no,
    previous_sale_page_no_start,
    prev_sale_page_no_end,
):

    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("<b>AGREEMENT OF SALE</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Introduction
    intro = (
        f"THIS AGREEMENT FOR SALE is made and executed on this the {datetime.now().strftime('%d')} day "
        f"{datetime.now().strftime('%B')} of {datetime.now().strftime('%Y')}."
    )
    elements.append(Paragraph(intro, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Parties
    elements.append(Paragraph("<b>BETWEEN</b>", styles["Normal"]))
    seller_details = (
        f"Mr. {seller_name} s/o. {seller_father_name}, aged {seller_age} years, residing at {seller_address}, "
        f'Hereinafter called "The SELLER" (which expression shall mean and include his/her legal heirs, '
        "successors, executors, administrators, legal representatives, and assigns) of ONE PART."
    )
    elements.append(Paragraph(seller_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AND</b>", styles["Normal"]))
    purchaser_details = (
        f"Mr. {purchaser_name} s/o {purchaser_father_name}, aged {purchaser_age} years, residing at "
        f'{purchaser_address}, hereinafter referred to as "The PURCHASER" (represented by his power of '
        "attorney, which expression shall include his heirs, successors, executors, administrators, "
        "legal representatives, and assigns) of the OTHER PART."
    )
    elements.append(Paragraph(purchaser_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Property details and conditions
    elements.append(Paragraph("<b>WHEREAS</b>", styles["Normal"]))
    property_details = (
        f'WHEREAS THE SELLER is the absolute owner in possession and enjoyment of the more fully described in the schedule hereunder and hereafter called the "SCHEDULE PROPERTY".\n'
        f"WHEREAS the property more fully described in the schedule hereunder is the self-acquired property of the SELLER, who purchased the same from Mr. {previous_owner} in and by sale deed dated {previous_sale_deed_date} and registered as Doct No. {previous_sale_doct_no} of Book1VolumeNo {previous_sale_book1_volumne_no} Pagenos.{previous_sale_page_no_start} to {prev_sale_page_no_end}, registered on and filed on the file of the Sub-Registrar.\n"
        f"WHEREAS the SELLER is the absolute owner of the property and has been enjoying the same with absolute right and has clear and marketable title to the Schedule Property.\n"
        f"WHEREAS the SELLER, being in need of funds for the purpose of {purpose_of_sale}, has decided to sell the property more fully described in the Schedule hereunder, and the PURCHASER has offered to purchase the same.\n"
        f"WHEREAS the SELLER offered to sell and transfer the schedule property to the PURCHASER for a sale consideration of Rs. {sale_amount} (Rupees {sale_amount} only), and the PURCHASER herein has agreed to purchase the same for the aforesaid consideration on the following terms and conditions."
    )
    elements.append(Paragraph(property_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Agreement Terms
    elements.append(
        Paragraph(f"<b>NOW THIS AGREEMENT WITNESSETH AS FOLLOWS:</b>", styles["Normal"])
    )
    terms = [
        f"The Sale consideration of the Schedule Property is fixed at Rs. {sale_amount} (Rupees {sale_amount} only).",
        f"The PURCHASER has paid a sum of Rs. {advance_amount} (Rupees {advance_amount} only) by cash/cheque/D.D. bearing No {cheque_no}, drawn on {bank_name}, dated {cheque_date} as advance, the receipt of which sum the SELLER hereby acknowledges.",
        f"The balance payment of Rs. {balance_amount} (Rupees {balance_amount} only) will be paid by the PURCHASER to the SELLER at the time of execution of the absolute Sale Deed, thus completing the sale transaction.",
        "The parties herein covenant to complete the Sale transaction and execute the Absolute Sale Deed by the end of the agreed transaction period.",
        "The SELLER confirms with the PURCHASER that he/she has not entered into any agreement for sale, mortgage, or exchange whatsoever with any other person relating to the Schedule Property of this Agreement.",
        "• The SELLER hereby assures the PURCHASER that he/she has absolute power to convey the same and that there are no encumbrances, liens, charges, Government dues, attachments, acquisition, or requisition proceedings, etc.",
        "The SELLER agrees to put the PURCHASER in absolute and vacant possession of the Schedule Property after executing the sale deed and registering the same in the jurisdictional Sub-Registrar's office.",
        "The SELLER covenants with the PURCHASER that he/she shall not do any act, deed, or thing creating any charge, lien, or encumbrance in respect of the Schedule Property during the subsistence of this Agreement.",
        "The SELLER has specifically agreed and covenants with the PURCHASER that he/she shall do all acts, deeds, and things necessary to convey absolute and marketable title to the Schedule Property in favor of the PURCHASER or his nominee.",
        "IT IS AGREED between the parties that all expenses towards Stamp Duty and Registration charges shall be borne by the PURCHASER only.",
        "• The PURCHASER shall have the right to nominate or assign his right under this agreement to any person/persons of his choice, and the SELLER shall execute the Sale Deed as per the terms and conditions of this Agreement in favor of the PURCHASER or his nominee or assignee.",
        f"• The SELLER has agreed to get a consent deed duly executed to this Sale transaction from his/her spouse ({seller_wife}), sons, and daughters ({seller_sons_daughters}) on or before the date of registration of the Sale Deed and assures that they will all join to execute the sale deed in favor of the PURCHASER.",
        "It is hereby expressly provided and agreed by the parties hereto that both parties are entitled to enforce specific performance of the agreement against each other in case of breach of any conditions mentioned in this Agreement.",
        "The original of the 'AGREEMENT' signed by both parties shall be with the PURCHASER, and a copy of the same, similarly signed, shall be with the SELLER.",
    ]

    for term in terms:
        elements.append(Paragraph(term, styles["Normal"]))
        elements.append(Spacer(1, 12))

    # Schedule Property
    elements.append(Paragraph(f"<b>SCHEDULE PROPERTY:</b>", styles["Normal"]))
    elements.append(Paragraph(schedule_property, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Closing
    elements.append(
        Paragraph(
            "IN WITNESS WHEREOF the SELLER and the PURCHASER have signed this Agreement in the presence of the following witnesses:",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Witnesses:", styles["Normal"]))
    elements.append(Paragraph(f"1. {witness_1}", styles["Normal"]))
    elements.append(Paragraph(f"2. {witness_2}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Signed by SELLER: __________________", styles["Normal"]))
    elements.append(
        Paragraph("Signed by PURCHASER: __________________", styles["Normal"])
    )

    # Build PDF
    doc.build(elements)


def generate_flat_sale_deed_pdf(
    file_name,
    seller_details,
    developer_details,
    confirming_party_details,
    purchaser_details,
    property_details,
    total_consideration,
    cheque_details,
    witness_1,
    witness_2,
    place,
):

    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("<b>DEED OF SALE OF FLAT</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Date
    date_intro = (
        f"This DEED OF SALE is made and executed at {place} on this {datetime.now().strftime('%d')} day "
        f"{datetime.now().strftime('%B')} of {datetime.now().strftime('%Y')}."
    )
    elements.append(Paragraph(date_intro, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Parties
    elements.append(Paragraph("<b>BETWEEN</b>", styles["Normal"]))
    seller_paragraph = (
        f"{seller_details['name']}, PAN {seller_details['pan']}, EPIC/Passport No. {seller_details['id_no']}, "
        f"Aadhar No. {seller_details['aadhar']}, son/daughter of {seller_details['father']}, "
        f"residing at {seller_details['address']}, by faith {seller_details['faith']}, "
        f"by Occupation {seller_details['occupation']}, by Nationality {seller_details['nationality']}, "
        "hereinafter referred to and called as the “OWNER(S)/VENDOR(S)”."
    )
    elements.append(Paragraph(seller_paragraph, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AND</b>", styles["Normal"]))
    developer_paragraph = (
        f"{developer_details['name']}, PAN {developer_details['pan']}, "
        f"having place of business at {developer_details['business_address']}, "
        f"represented by its Partner(s) {developer_details['partner']}, "
        f"son/daughter of {developer_details['partner_father']}, "
        f"residing at {developer_details['partner_address']}, by faith {developer_details['faith']}, "
        f"by Occupation {developer_details['occupation']}, "
        f"by Nationality {developer_details['nationality']}, "
        "hereinafter referred to and called as the ‘DEVELOPER(s)’"
    )
    elements.append(Paragraph(developer_paragraph, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AND</b>", styles["Normal"]))
    confirming_party_paragraph = (
        f"{confirming_party_details['name']}, PAN {confirming_party_details['pan']}, "
        f"EPIC/Passport No. {confirming_party_details['id_no']}, "
        f"Aadhar No. {confirming_party_details['aadhar']}, "
        f"son/daughter of {confirming_party_details['father']}, "
        f"residing at {confirming_party_details['address']}, by faith {confirming_party_details['faith']}, "
        f"by Occupation {confirming_party_details['occupation']}, "
        f"by Nationality {confirming_party_details['nationality']}, "
        "hereinafter referred to and called as the “CONFIRMING PARTY (IES)”."
    )
    elements.append(Paragraph(confirming_party_paragraph, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AND</b>", styles["Normal"]))
    purchaser_paragraph = (
        f"{purchaser_details['name']}, PAN {purchaser_details['pan']}, "
        f"EPIC/Passport No. {purchaser_details['id_no']}, "
        f"Aadhar No. {purchaser_details['aadhar']}, "
        f"son/daughter of {purchaser_details['father']}, "
        f"residing at {purchaser_details['address']}, by faith {purchaser_details['faith']}, "
        f"by Occupation {purchaser_details['occupation']}, "
        f"by Nationality {purchaser_details['nationality']}, "
        "hereinafter referred to and called as the “Purchaser (S)”."
    )
    elements.append(Paragraph(purchaser_paragraph, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Terms of Sale
    elements.append(
        Paragraph("<b>NOW THIS DEED WITNESSETH AS UNDER:</b>", styles["Normal"])
    )
    elements.append(
        Paragraph(
            f"In consideration of Rs {total_consideration} (Rupees {total_consideration} only), the entire amount has been received by the Vendor from the Purchaser prior to the execution of this sale deed.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))
    elements.append(
        Paragraph(
            "1. The Vendor hereby sells, conveys and assigns the property absolutely and forever to the Purchaser.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))
    elements.append(
        Paragraph(
            "2. The actual physical possession of the said property has been handed over by the Vendor to the Purchaser.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))
    elements.append(
        Paragraph(
            "3. The Vendor hereby assures the Purchaser that the property is free from all encumbrances.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))

    # Schedule of Property
    elements.append(Paragraph("<b>THE SCHEDULE “A”</b>", styles["Normal"]))
    schedule_details = (
        f"All that piece and parcel of a demarcated self-contained residential flat being No. {property_details['flat_number']} "
        f"on the {property_details['floor']} Floor, in Block {property_details['block']}, having measurement of "
        f"{property_details['size']} sq. ft., with {property_details['amenities']} within the said Complex."
    )
    elements.append(Paragraph(schedule_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Witnesses
    elements.append(
        Paragraph(
            "IN WITNESS WHEREOF the parties hereto have hereunto set and subscribed their respective hands and seals.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))
    elements.append(
        Paragraph(f"Signed by the Vendor: __________________", styles["Normal"])
    )
    elements.append(
        Paragraph(f"Signed by the Purchaser: __________________", styles["Normal"])
    )
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("WITNESSES:", styles["Normal"]))
    elements.append(Paragraph(f"1. {witness_1}", styles["Normal"]))
    elements.append(Paragraph(f"2. {witness_2}", styles["Normal"]))

    # Build PDF
    doc.build(elements)


def generate_land_sale_deed_pdf(
    file_name,
    seller_name,
    seller_father_name,
    seller_age,
    seller_pan,
    seller_address,
    purchaser_name,
    purchaser_father_name,
    purchaser_age,
    purchaser_pan,
    purchaser_address,
    land_details,
    total_consideration,
    cheque_details,
    witness_1,
    witness_2,
):

    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("<b>DEED OF SALE</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Introduction
    intro = (
        f"This DEED OF SALE is made and executed on this {datetime.now().strftime('%d')} day "
        f"{datetime.now().strftime('%B')} of {datetime.now().strftime('%Y')}."
    )
    elements.append(Paragraph(intro, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Parties
    elements.append(Paragraph("<b>BETWEEN</b>", styles["Normal"]))
    seller_details = (
        f"Sri {seller_name}, son of {seller_father_name}, aged about {seller_age} years, "
        f"Holding PAN {seller_pan}, residing at {seller_address}, "
        f"hereinafter called the “SELLER”."
    )
    elements.append(Paragraph(seller_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AND</b>", styles["Normal"]))
    purchaser_details = (
        f"Sri {purchaser_name}, son of {purchaser_father_name}, aged about {purchaser_age} years, "
        f"Holding PAN {purchaser_pan}, residing at {purchaser_address}, "
        f"hereinafter called the “PURCHASER”."
    )
    elements.append(Paragraph(purchaser_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Property details and conditions
    elements.append(Paragraph("<b>WHEREAS</b>", styles["Normal"]))
    property_details = (
        f"WHEREAS the SELLER is the absolute owner of the land measuring about {land_details['size']}, "
        f"lying and situated in {land_details['location']}, described in the schedule hereunder referred to as the “SCHEDULE PROPERTY”.\n"
        f"WHEREAS the SELLER is willing to sell the SCHEDULE PROPERTY to the PURCHASER for a total consideration of "
        f"Rs. {total_consideration} (Rupees {total_consideration} only) and the PURCHASER has agreed to purchase the same."
    )
    elements.append(Paragraph(property_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Agreement Terms
    elements.append(
        Paragraph("<b>NOW THIS DEED OF SALE WITNESSETH:</b>", styles["Normal"])
    )
    terms = [
        f"1. The SELLER hereby sells, conveys, transfers, and assigns unto the PURCHASER the SCHEDULE PROPERTY.",
        f"2. The consideration of Rs. {total_consideration} has been received by the SELLER in cash/cheque/bank draft: {cheque_details}.",
        "3. The SELLER warrants that the SCHEDULE PROPERTY is free from all encumbrances, mortgages, and claims.",
        "4. The SELLER agrees to provide vacant possession of the SCHEDULE PROPERTY to the PURCHASER.",
        "5. The SELLER shall execute all necessary documents to perfect the title of the PURCHASER.",
        "6. The SELLER confirms that all taxes related to the property are paid up to the date of this sale.",
        "7. The PURCHASER is entitled to mutation of title in all public records.",
    ]

    for term in terms:
        elements.append(Paragraph(term, styles["Normal"]))
        elements.append(Spacer(1, 12))

    # Schedule of Property
    elements.append(Paragraph("<b>SCHEDULE OF PROPERTY:</b>", styles["Normal"]))
    schedule_details = (
        f"All that piece and parcel of land measuring about {land_details['size']} "
        f"lying and situated in {land_details['location']}, butted and bounded by:\n"
        f"On the North: {land_details['boundaries']['north']}\n"
        f"On the South: {land_details['boundaries']['south']}\n"
        f"On the East: {land_details['boundaries']['east']}\n"
        f"On the West: {land_details['boundaries']['west']}"
    )
    elements.append(Paragraph(schedule_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Closing
    closing = "IN WITNESS WHEREOF the SELLER and the PURCHASER have set their signatures on the day, month and year first above written."
    elements.append(Paragraph(closing, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph("Signed by the SELLER: __________________", styles["Normal"])
    )
    elements.append(
        Paragraph("Signed by the PURCHASER: __________________", styles["Normal"])
    )
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("WITNESSES:", styles["Normal"]))
    elements.append(Paragraph(f"1. {witness_1}", styles["Normal"]))
    elements.append(Paragraph(f"2. {witness_2}", styles["Normal"]))

    # Build PDF
    doc.build(elements)


def generate_non_disclosure_agreement_pdf(
    file_name,
    company_name,
    company_address,
    employee_name,
    employee_address,
    high_court_city,
):
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(
        Paragraph(
            "<b>EMPLOYEE NON-DISCLOSURE & NON-COMPETE AGREEMENT</b>", styles["Title"]
        )
    )
    elements.append(Spacer(1, 12))

    # Date
    date_intro = (
        f"This EMPLOYEE NON-DISCLOSURE & NON-COMPETE AGREEMENT has been entered into this "
        f"{datetime.now().strftime('%d')} day of {datetime.now().strftime('%B')}, {datetime.now().strftime('%Y')}."
    )
    elements.append(Paragraph(date_intro, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # BETWEEN Clause
    between_clause = (
        f"BETWEEN\n\n{company_name}, an Indian [Company / Firm / LLP / Partnership] having its registered office at "
        f"{company_address} (hereinafter called {company_name.split()[0]} which expression unless repugnant "
        f"to the context shall mean and include its subsidiaries, and its successors and assigns).\n\n"
        f"AND\n\n{employee_name}, an Employee of {company_name.split()[0]} and residing at "
        f"{employee_address} (hereinafter referred to as 'Employee' which expression unless repugnant "
        f"to the context shall include all beneficiaries of the said employee)."
    )
    elements.append(Paragraph(between_clause, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Definitions
    elements.append(Paragraph("<b>1. Definitions</b>", styles["Normal"]))
    definitions = (
        "<b>Intellectual Property:</b> Includes existing and future Intellectual Property in the nature of unregistered or "
        "registered rights to any and all patents, copyrights, trademarks, and other confidential and/or proprietary information limited "
        "to that forming part of the subject matter of the agreement, and inclusive of all intellectual property owned by "
        f"{company_name.split()[0]} and/or its subsidiaries, venture partners, and predecessors in interest, arising out of the performance of this agreement "
        "and/or other business arrangements.\n\n"
        "<b>Confidential Information:</b> Confidential information means, trade secrets, know-how, patents, utility models, formulations, "
        "processes/methods of preparation, test data, conducted in-house or through collaborative efforts, and any and all improvements, modifications, "
        "or alterations that may have been effected to the said Confidential Information by the Company. Confidential information includes, but is not limited to:\n"
        "(i) The terms and conditions of this Agreement or any prior agreement; (ii) Company's business plans, strategies, methods, and practices; "
        "(iii) Information about Company's Personnel, products, customers, marketing strategies, services, or future business plans; "
        "(iv) Process information, including data, reports, studies, test data, and practical instructions related to any product."
    )
    elements.append(Paragraph(definitions, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Acknowledgment of Confidentiality
    elements.append(
        Paragraph("<b>2. Acknowledgment of Confidentiality</b>", styles["Normal"])
    )
    ack_of_confidentiality = (
        f"{employee_name} hereby acknowledges that the intellectual property and/or confidential "
        f"information are in the nature of confidential and proprietary information owned by {company_name.split()[0]}."
    )
    elements.append(Paragraph(ack_of_confidentiality, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Agreement Not to Disclose
    elements.append(Paragraph("<b>3. Agreement Not to Disclose</b>", styles["Normal"]))
    agreement_not_to_disclose = (
        f"a. {employee_name} hereby agrees that he/she shall hold in confidence and not use, commercialize, or disclose any "
        f"confidential information or intellectual property except under the terms of employment with {company_name.split()[0]} "
        "or as authorized in writing by the Company.\n\n"
        "b. Even upon assignment of confidential information or intellectual property to the Company, the employee undertakes to use at least "
        "the same degree of care in safeguarding the confidential information as they use in safeguarding their own confidential information."
    )
    elements.append(Paragraph(agreement_not_to_disclose, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Remedies for Breach
    elements.append(
        Paragraph("<b>4. Remedies for Breach of Confidentiality</b>", styles["Normal"])
    )
    remedies = (
        f"{employee_name} agrees that any disclosure of confidential information prohibited herein or breach of the provisions may result in "
        f"irreparable injury and damage to {company_name.split()[0]}. The Company may seek legal remedies, including preliminary, temporary, "
        "or permanent injunctions, as necessary to protect its interests. The employee agrees to reimburse reasonable legal fees and other costs incurred."
    )
    elements.append(Paragraph(remedies, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Non-Compete Clause
    elements.append(Paragraph("<b>5. Non-Compete</b>", styles["Normal"]))
    non_compete = (
        f"{employee_name} agrees not to directly or indirectly compete with the business of {company_name.split()[0]} for a "
        "period of 5 years following the expiration or termination of this agreement, regardless of the cause."
    )
    elements.append(Paragraph(non_compete, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Jurisdiction
    elements.append(Paragraph("<b>6. Jurisdiction</b>", styles["Normal"]))
    jurisdiction = (
        f"Any action arising out of or pertaining to this agreement shall be initiated and maintained in a court of competent jurisdiction "
        f"at the High Court of {high_court_city}."
    )
    elements.append(Paragraph(jurisdiction, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # General Provisions
    elements.append(Paragraph("<b>7. General Provisions</b>", styles["Normal"]))
    general_provisions = (
        "a. This document constitutes the entire agreement between the parties and supersedes all prior communications, whether written or oral.\n\n"
        "b. This Agreement is limited to its terms and may be modified only by writing signed by both parties.\n\n"
        "c. Neither this Agreement nor any rights or obligations inherent in the Company's Confidential Information, trade secrets, or intellectual property may "
        "be transferred without written consent."
    )
    elements.append(Paragraph(general_provisions, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Severability
    elements.append(Paragraph("<b>8. Severability</b>", styles["Normal"]))
    severability = (
        "The provisions of this agreement are severable. If any provision is deemed unenforceable, the remaining provisions will remain in full force and effect. "
        "The parties will substitute an enforceable provision that preserves the original intent."
    )
    elements.append(Paragraph(severability, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Force Majeure
    elements.append(Paragraph("<b>9. Force Majeure</b>", styles["Normal"]))
    force_majeure = (
        "Neither party will be responsible for any failure to perform its obligations due to causes beyond its control, such as acts of God, war, riots, embargoes, "
        "fire, floods, or accidents."
    )
    elements.append(Paragraph(force_majeure, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Notice
    elements.append(Paragraph("<b>10. Notice</b>", styles["Normal"]))
    notice = "All notices and communications required under this agreement shall be in writing and considered delivered if received in person, or 15 days after mailing by registered post."
    elements.append(Paragraph(notice, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Closing
    closing = "IN WITNESS WHEREOF, the parties have executed this Agreement on the date first written above by their duly authorized representatives."
    elements.append(Paragraph(closing, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(f"Signed for {company_name}: __________________", styles["Normal"])
    )
    elements.append(
        Paragraph(f"Signed by {employee_name}: __________________", styles["Normal"])
    )
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("WITNESSES:", styles["Normal"]))
    elements.append(Paragraph("1. __________________", styles["Normal"]))
    elements.append(Paragraph("2. __________________", styles["Normal"]))

    # Build PDF
    doc.build(elements)


# Example data for the agreement


def generate_will_deed_pdf(
    file_name,
    testator_name,
    father_name,
    testator_address,
    testator_age,
    religion,
    occupation,
    executors,
    family_members,
    property_details,
    wife_name,
    children_details,
    witness_1_name,
    witness_2_name,
    day_of_contract,
    month_of_contract,
    year_of_contract,
    witness_1_address,
    witness_2_address,
):
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("<b>WILL-DEED</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Introductory Clause
    intro = (
        f"I <b>Sri. {testator_name}</b> S/o. <b>{father_name}</b>, residing at <b>{testator_address}</b>, aged about <b>{testator_age}</b> years, "
        f"<b>{religion}</b> by religion, occupation <b>{occupation}</b>, do make this my last will and testament."
    )
    elements.append(Paragraph(intro, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Revocation Clause
    revocation = (
        "1. I have not made any will or other testamentary document, but if any made, I hereby revoke all previous wills "
        "and codicils, if any, and declare this to be my last will and testament."
    )
    elements.append(Paragraph(revocation, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Executors
    elements.append(
        Paragraph(
            "2. I appoint the following individuals as executors and trustees of my estate:",
            styles["Normal"],
        )
    )
    for i, executor in enumerate(executors, 1):
        executor_text = (
            f"{i}. <b>Sri. {executor['name']}</b> S/o. <b>{executor['father_name']}</b>, residing at <b>{executor['address']}</b>, "
            f"aged about <b>{executor['age']}</b> years, <b>{executor['religion']}</b> by religion, occupation <b>{executor['occupation']}</b>."
        )
        elements.append(Paragraph(executor_text, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Family Members
    elements.append(Paragraph("3. My family consists of:", styles["Normal"]))
    family_text = f"<b>{', '.join(family_members)}</b>."
    elements.append(Paragraph(family_text, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Property Details
    elements.append(Paragraph("4. My property consists of:", styles["Normal"]))
    for i, property_item in enumerate(property_details, 1):
        elements.append(
            Paragraph(f"({chr(96 + i)}) <b>{property_item}</b>", styles["Normal"])
        )
    elements.append(Spacer(1, 12))

    # Bequeath to Wife
    bequeath_text = (
        f"5. I bequeath all my property in whatever form existing at the time of my death to the said executor and trustees "
        f"to hold the same on trust for the benefit of my wife <b>Smt. {wife_name}</b> for her lifetime."
    )
    elements.append(Paragraph(bequeath_text, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Income and Expenses Clause
    elements.append(
        Paragraph(
            "6. My executors and trustees shall manage the property and pay the net income to my wife. "
            "They may also use the corpus of the estate for her medical expenses or pilgrimage but may not sell or mortgage the immovable property.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))

    # Children Clause
    elements.append(
        Paragraph(
            "7. On the death of my wife, or if she predeceases me, then on my death, all my estate will belong to my children:",
            styles["Normal"],
        )
    )
    for i, child in enumerate(children_details, 1):
        elements.append(Paragraph(f"({chr(96 + i)}) <b>{child}</b>", styles["Normal"]))
    elements.append(
        Paragraph(
            "The estate shall be equally divided among them, and the executors will transfer the property accordingly.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))

    # Minors Clause
    elements.append(
        Paragraph(
            "8. If any of my children is a minor at the time of my death, the trustees shall hold the property in trust until the youngest attains the age of majority. "
            "The income will be used for the children's maintenance and education.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))

    # Probate Clause
    elements.append(
        Paragraph(
            "9. My executors shall obtain probate from a competent court, if required, and pay all necessary duties and expenses, "
            "as well as any taxes or liabilities.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))

    # Closing Clause
    elements.append(
        Paragraph(
            "10. I make this will of my own free will, being in sound health and mind, and in witness thereof, I have signed this will in the presence of witnesses "
            f"on this {day_of_contract} day of {month_of_contract} month of {year_of_contract} year.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))

    # Signature
    elements.append(Paragraph("Signed by the testator:", styles["Normal"]))
    elements.append(Paragraph(f"<b>Sri. {testator_name}</b>", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Witnesses
    elements.append(Paragraph("WITNESSES:", styles["Normal"]))
    elements.append(Paragraph(f"1. {witness_1_name}", styles["Normal"]))
    elements.append(Paragraph(f"Full Address:{witness_1_address}", styles["Normal"]))
    elements.append(Paragraph(f"2. {witness_2_name}", styles["Normal"]))
    elements.append(Paragraph(f"Full Address: {witness_2_address}", styles["Normal"]))

    # Build PDF
    doc.build(elements)


import json
import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


class LeaveAndLicenseGenerator:
    def __init__(self, json_data):
        self.data = json.loads(json_data)
        self.styles = getSampleStyleSheet()
        self.custom_styles()

    def custom_styles(self):
        self.styles["Normal"].alignment = 4  # 4 is for justified text
        self.styles["Heading1"].fontSize = 14
        self.styles["Heading1"].spaceAfter = 12
        self.styles["Heading2"].fontSize = 12
        self.styles["Heading2"].spaceAfter = 6
        self.styles.add(
            ParagraphStyle(name="Justify", parent=self.styles["Normal"], alignment=4)
        )
        self.styles.add(
            ParagraphStyle(
                name="Bold", parent=self.styles["Normal"], fontName="Helvetica-Bold"
            )
        )

    def generate_pdf(self, output_path="leave_and_license_agreement.pdf"):
        doc = SimpleDocTemplate(
            output_path,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18,
        )

        story = []
        self.add_title(story)
        self.add_stamp_duty(story)
        self.add_parties(story)
        self.add_whereas_clauses(story)
        self.add_agreement_clauses(story)
        self.add_schedule(story)
        self.add_signatures(story)

        doc.build(story)
        print(f"PDF generated and saved as: {output_path}")

    def add_title(self, story):
        story.append(Paragraph("Leave and License Agreement", self.styles["Heading1"]))
        story.append(Spacer(1, 12))

    def add_stamp_duty(self, story):
        data = [
            ["Particulars", "Amount Paid", "GRN No.", "Date"],
            [
                "Stamp Duty",
                f"Rs. {self.data['stamp_duty']}/-",
                self.data["stamp_duty_grn"],
                self.data["stamp_duty_date"],
            ],
            [
                "Registration Fee",
                f"Rs. {self.data['registration_fee']}/-",
                self.data["registration_grn"],
                self.data["registration_date"],
            ],
        ]
        t = Table(data)
        t.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 12),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                    ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                    ("FONTSIZE", (0, 1), (-1, -1), 10),
                    ("TOPPADDING", (0, 1), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, -1), (-1, -1), 6),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ]
            )
        )
        story.append(t)
        story.append(Spacer(1, 12))

    def add_parties(self, story):
        story.append(
            Paragraph(
                f"This agreement is made and executed on {self.data['date']} at {self.data['city']}",
                self.styles["Normal"],
            )
        )
        story.append(Paragraph("Between,", self.styles["Normal"]))
        story.append(Spacer(1, 12))

        licensor_details = (
            f"{self.data['licensor_name']}, Age: About {self.data['licensor_age']} Years, "
            f"Occupation: {self.data['licensor_occupation']}, "
            f"PAN: {self.data['licensor_pan']}, UID: {self.data['licensor_uid']}"
            f"\nResiding at: {self.data['licensor_address']}"
        )
        story.append(Paragraph(licensor_details, self.styles["Normal"]))
        story.append(Spacer(1, 12))

        story.append(
            Paragraph(
                "HEREINAFTER called 'the Licensor' (which expression shall mean and include the Licensor above named as also his respective heirs, successors, assigns, executors and administrators)",
                self.styles["Normal"],
            )
        )
        story.append(Paragraph("AND", self.styles["Normal"]))
        story.append(Spacer(1, 12))

        licensee_details = (
            f"{self.data['licensee_name']}, Age: About {self.data['licensee_age']} Years, "
            f"Occupation: {self.data['licensee_occupation']}, "
            f"PAN: {self.data['licensee_pan']}, UID: {self.data['licensee_uid']}"
            f"\nResiding at: {self.data['licensee_address']}"
        )
        story.append(Paragraph(licensee_details, self.styles["Normal"]))
        story.append(Spacer(1, 12))

        story.append(
            Paragraph(
                "HEREINAFTER called 'the Licensee'(which expression shall mean and include only Licensee above named).",
                self.styles["Normal"],
            )
        )
        story.append(Spacer(1, 12))

    def add_whereas_clauses(self, story):
        story.append(Paragraph("Whereas Clauses", self.styles["Heading2"]))

        whereas_text = (
            "WHEREAS the Licensor is absolutely seized and possessed of and or otherwise well and "
            "sufficiently entitled to all that constructed portion being unit described in Schedule "
            "hereunder written and are hereafter for the sake of brevity called or referred to as "
            "Licensed Premises and is/are desirous of giving the said premises on Leave and License "
            "basis under Section 24 of the Maharashtra Rent Control Act, 1999."
            "\n\nAND WHEREAS the Licensee herein is in need of temporary premises for his use and "
            "has/have approached the Licensor with a request to allow the Licensee herein to use and "
            f"occupy the said premises on Leave and License basis for a period of {self.data['period']} "
            f"Months commencing from {self.data['start_date']} and ending on {self.data['end_date']}, "
            "on terms and subject to conditions hereafter appearing."
            "\n\nAND WHEREAS the Licensor have agreed to allow the Licensee herein to use and occupy the "
            "said Licensed premises for his aforesaid purposes only, on Leave and License basis for "
            "above mentioned period, on terms and subject to conditions hereafter appearing;"
        )
        story.append(Paragraph(whereas_text, self.styles["Justify"]))
        story.append(Spacer(1, 12))

    def add_agreement_clauses(self, story):
        story.append(Paragraph("Agreement Clauses", self.styles["Heading2"]))

        story.append(
            Paragraph(
                "NOW THEREFORE IT IS HEREBY AGREED TO, DECLARED AND RECORDED BY AND BETWEEN THE PARTIES HERETO AS FOLLOWS:-",
                self.styles["Normal"],
            )
        )
        story.append(Spacer(1, 12))

        clauses = [
            (
                "1) Period: ",
                f"That the Licensor hereby grants to the Licensee herein a revocable leave and license, to occupy the Licensed Premises, described in Schedule hereunder written without creating any tenancy rights or any other rights, title and interest in favour of the Licensee for a period of {self.data['period']} Months commencing from {self.data['start_date']} and ending on {self.data['end_date']}",
            ),
            (
                "2) Rent & Deposit: ",
                f"That the Licensee shall pay to the Licensor Rs. {self.data['monthly_rent']} per month towards the compensation and Rs. {self.data['deposit']} interest free refundable deposit, for the use of the said licensed premises. The amount of monthly compensation shall be payable within first five days of the concerned month of Leave and License.",
            ),
            (
                "3) Payment of Deposit: ",
                f"That the Licensee have paid the above mentioned deposit of Rs. {self.data['deposit']} by {self.data['deposit_payment_method']}.",
            ),
            (
                "4) Maintenance Charges: ",
                f"That the {self.data['maintenance_charges_paid_by']} shall bear and pay all the maintenance charges in respect of the said Licensed Premises, and other outgoings including all rates, taxes, levies, assessment, non occupancy charges, etc. in respect of the said premises.",
            ),
            (
                "5) Use: ",
                f"That the Licensed premises shall only be used by the Licensee for {self.data['purpose']} purpose. The Licensee shall maintain the said premises in its existing condition and damage, if any, caused to the said premises, the same shall be repaired by the Licensee at its own cost subject to normal wear and tear. The Licensee shall not do anything in the said premises which is or is likely to cause a nuisance to the other occupants of the said building or to the prejudice in any manner to the rights of Licensor in respect of said premises or shall not do any unlawful activities prohibited by State or Central Government.",
            ),
            (
                "6) Alteration: ",
                "That the Licensee shall not make or permit to be made any alteration or addition to the construction or arrangements (internal or external) of the Licensed premises without obtaining prior written consent from the Licensor.",
            ),
            (
                "7) No Tenancy: ",
                "That the Licensee shall not claim any tenancy rights and shall not have any right to transfer, assign, sublet, or grant any license or sub-license concerning the Licensed premises or any part thereof. Additionally, the Licensee shall not mortgage or raise any loan against the said premises.",
            ),
            (
                "8) Inspection: ",
                "That the Licensor shall have the right to access the Licensed premises, either personally or through an authorized representative, to enter, view, and inspect the premises at reasonable intervals, provided reasonable notice is given to the Licensee.",
            ),
            (
                "9) Cancellation: ",
                "That if the Licensee defaults in making regular and punctual payments of monthly compensation as mentioned herein, or commits a breach of any of the terms, covenants, and conditions of this agreement, or if any legislation prohibiting the Leave and License is imposed, the Licensor shall be entitled to revoke and/or cancel the License granted herein by giving one month's notice in writing. The Licensee shall also have the right to vacate the said premises by providing one month's written notice to the Licensor as mentioned earlier.",
            ),
            (
                "10) Possession: ",
                "That immediately upon the expiration, termination, or cancellation of this agreement, the Licensee shall vacate the said premises without delay along with all personal belongings. In the event that the Licensee fails to remove themselves and/or their belongings from the said premises upon expiry or termination of this Agreement, the Licensor shall be entitled to recover damages at a rate of double the daily amount of compensation per day. Alternatively, the Licensor shall have the right to remove the Licensee and their belongings from the Licensed premises without recourse to the Court of Law.",
            ),
            (
                "11) Registration: ",
                "This Agreement shall be registered, and the Licensee shall bear all expenses related to stamp duty, registration fees, and any incidental charges, if applicable.",
            ),
        ]

        for title, content in clauses:
            story.append(Paragraph(title, self.styles["Bold"]))
            story.append(Paragraph(content, self.styles["Justify"]))
            story.append(Spacer(1, 6))

    def add_schedule(self, story):
        story.append(Paragraph("Schedule", self.styles["Heading2"]))

        schedule_text = (
            f"All that constructed portion being residential unit bearing "
            f"{self.data['flat_number']}, Built-up Area: {self.data['built_up_area']}, "
            f"situated on the {self.data['floor']} Floor of a Building known as {self.data['building_name']} "
            f"standing on the plot of land bearing {self.data['plot_details']}, "
            f"of Village: {self.data['village']}, situated within the revenue limits of "
            f"Tehsil {self.data['tehsil']} and Dist {self.data['district']} and situated within "
            f"the limits of {self.data['municipal_corporation']} Municipal Corporation."
        )
        story.append(Paragraph(schedule_text, self.styles["Justify"]))
        story.append(Spacer(1, 12))

    def add_signatures(self, story):
        story.append(Paragraph("Signatures", self.styles["Heading2"]))

        signature_text = (
            "IN WITNESS WHEREOF the parties hereto have set and subscribed their respective signatures "
            "by way of putting thumb impression electronic signature hereto in the presence of witness,"
            "who are identifying the executants, on the day, month and year first above written."
        )
        story.append(Paragraph(signature_text, self.styles["Justify"]))
        story.append(Spacer(1, 12))

        # Define the data for the signature table
        data = [
            ["Name & Address", "Photo", "Thumb Impression", "Digitally Signed"],
            ["Licensee", "", "", ""],
            [f"Name: {self.data['licensee_name']}", "", "", ""],
            [f"UID: {self.data['licensee_uid']}", "", "", ""],
            [f"Address: {self.data['licensee_address']}", "", "", ""],
            ["Licensor", "", "", ""],
            [f"Name: {self.data['licensor_name']}", "", "", ""],
            [f"UID: {self.data['licensor_uid']}", "", "", ""],
            [f"Address: {self.data['licensor_address']}", "", "", ""],
            ["Witness 1", "", "", ""],
            ["Witness 2", "", "", ""],
        ]

        # Create the table for the signatures section
        t = Table(data, colWidths=[2.5 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch])
        t.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 12),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                    ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                    ("FONTSIZE", (0, 1), (-1, -1), 10),
                    ("TOPPADDING", (0, 1), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, -1), (-1, -1), 6),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ]
            )
        )

        story.append(t)
        story.append(Spacer(1, 12))


json_data = """
{
    "date": "September 27, 2024",
    "city": "Mumbai",
    "stamp_duty": 5000,
    "stamp_duty_grn": "GRN123456",
    "stamp_duty_date": "2024-09-15",
    "registration_fee": 1000,
    "registration_grn": "GRN654321",
    "registration_date": "2024-09-16",
    "licensor_name": "John Doe",
    "licensor_age": "45",
    "licensor_occupation": "Business",
    "licensor_pan": "ABCDE1234F",
    "licensor_uid": "1234 5678 9012",
    "licensor_address": "123 Main St, Mumbai",
    "licensee_name": "Jane Smith",
    "licensee_age": "30",
    "licensee_occupation": "Software Engineer",
    "licensee_pan": "FGHIJ5678K",
    "licensee_uid": "9876 5432 1098",
    "licensee_address": "456 Park Ave, Mumbai",
    "period": "11",
    "start_date": "October 1, 2024",
    "end_date": "August 31, 2025",
    "monthly_rent": "25000",
    "deposit": "100000",
    "deposit_payment_method": "NEFT",
    "maintenance_charges_paid_by": "Licensee",
    "purpose": "residential",
    "flat_number": "A-101",
    "built_up_area": "1000 sq ft",
    "floor": "1st",
    "building_name": "Sunshine Apartments",
    "plot_details": "Plot No. 45, Sector 10",
    "village": "Andheri",
    "tehsil": "Andheri",
    "district": "Mumbai Suburban",
    "municipal_corporation": "Mumbai"
}
"""
# # Correct: 'agreement' is an instance of LicenseAgreement
# agreement = LeaveAndLicenseGenerator(json_data)
# agreement.generate_pdf("samyak-whale-legal-lla.pdf")

# import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


class NDAGenerator:
    def __init__(self, json_data):
        self.data = json.loads(json_data)
        self.styles = getSampleStyleSheet()
        self.custom_styles()

    def custom_styles(self):
        self.styles["Normal"].alignment = 4  # 4 is for justified text
        self.styles["Heading1"].fontSize = 14
        self.styles["Heading1"].spaceAfter = 12
        self.styles["Heading2"].fontSize = 12
        self.styles["Heading2"].spaceAfter = 6
        self.styles.add(
            ParagraphStyle(name="Justify", parent=self.styles["Normal"], alignment=4)
        )

    def generate_pdf(self, output_path=None):
        if output_path is None:
            output_path = "non_disclosure_agreement.pdf"

        doc = SimpleDocTemplate(
            output_path,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18,
        )

        story = []
        self.add_title(story)
        self.add_parties(story)
        self.add_whereas(story)
        self.add_agreement_clauses(story)
        self.add_signatures(story)

        doc.build(story)
        print(f"PDF generated and saved as: {output_path}")

    def add_title(self, story):
        story.append(Paragraph("Non-Disclosure Agreement", self.styles["Heading1"]))
        story.append(Spacer(1, 12))
        story.append(
            Paragraph(
                f"This non-disclosure agreement (\"Agreement\") is dated {self.data['effective_date']} (\"Effective Date\") and is entered into by and between:",
                self.styles["Normal"],
            )
        )
        story.append(Spacer(1, 12))

    def add_parties(self, story):
        story.append(
            Paragraph(self.data["party1_name"] + f' ("Party 1")', self.styles["Normal"])
        )
        story.append(Spacer(1, 12))
        story.append(Paragraph("AND", self.styles["Normal"]))
        story.append(Spacer(1, 12))
        story.append(
            Paragraph(self.data["party2_name"] + f' ("Party 2")', self.styles["Normal"])
        )
        story.append(Spacer(1, 12))
        story.append(
            Paragraph(
                'Party 1 and Party 2 are hereinafter referred to individually as a "Party" and collectively as the "Parties". Wherever the context requires, the Party disclosing the confidential information shall be referred to as the "Disclosing Party" and the Party receiving the confidential information shall be referred to as the "Receiving Party".',
                self.styles["Justify"],
            )
        )
        story.append(Spacer(1, 12))

    def add_whereas(self, story):
        story.append(Paragraph("Whereas:", self.styles["Heading2"]))
        story.append(
            Paragraph(
                f"A. Party 1 engages in {self.data['party1_business']} and Party 2 engages in {self.data['party2_business']}.",
                self.styles["Normal"],
            )
        )
        story.append(
            Paragraph(
                f"B. The Parties wish to collaborate and enter into discussions for the purpose of {self.data['purpose']} (\"Purpose\") and wish to keep such discussions confidential.",
                self.styles["Normal"],
            )
        )
        story.append(Spacer(1, 12))

    def add_agreement_clauses(self, story):
        story.append(
            Paragraph(
                "Now therefore, in consideration for the mutual promises and covenants set forth herein, the Parties agree as follows:",
                self.styles["Normal"],
            )
        )
        story.append(Spacer(1, 12))

        clauses = [
            '"Confidential Information" shall mean and include all non-public information, written or oral, disclosed, directly or indirectly, through any means of communication or observation (including oral, graphic, written or electronic form) by the Disclosing Party or any of its affiliates or representatives to or for the benefit of the Receiving Party from the Effective Date, irrespective of whether such information: (a) has been specifically marked as "confidential" at the time of disclosure; (b) is treated as proprietary information by the Disclosing Party; or (c) is owned or developed by the Disclosing Party.',
            "Confidential Information shall include any financial, business, proprietary or technical information of the Disclosing Party.",
            "All such Confidential Information shared under this Agreement shall be used by the Parties exclusively for the Purpose and neither Party shall disclose or otherwise use the Confidential Information for any other purpose or in any other manner without the prior written approval of the Disclosing Party.",
            "The Confidential Information shared under this Agreement may be disclosed by the Receiving Party to other employees on a need to know basis, with written consent from the Disclosing Party, in connection with the Purpose, and who shall protect the Confidential Information in accordance with the terms of this Agreement.",
            "The Receiving Party shall protect the Confidential Information in the same manner as it would protect its own confidential information.",
            "The confidentiality obligations under this Agreement shall not apply to Confidential Information which:",
            "Notwithstanding anything to the contrary contained in this Agreement, Confidential Information may be disclosed as required by applicable law, regulations or governmental procedure, provided the Receiving Party notifies the Disclosing Party prior to such disclosure, unless prohibited by law, so as to afford the Disclosing Party reasonable opportunity to object or seek an appropriate protective order with respect to such disclosure.",
            "The Receiving Party agrees not to issue or release for publication any articles or advertising or publicity matter relating to this Agreement which mention or imply the name of the Disclosing Party any of its affiliates, or subject matter hereof, unless prior written consent is granted by the Disclosing Party subject only to Clause 7. The Receiving Party shall make such amendments to any such press release or public statement as are reasonably requested by the Disclosing Party.",
            "No transfer of intellectual property right either by way of assignment or license is either granted or implied by the disclosure of Confidential Information to the Receiving Party. The fact that Confidential Information is disclosed to the Receiving Party shall not be deemed to constitute any representation, warranty or inducement by the Disclosing Party of any kind (including of its accuracy or correctness) with respect to the Confidential Information, including without limitation, which such use will not infringe on intellectual property rights of any third party.",
            "The Receiving Party shall, upon the request of the Disclosing Party or upon the termination of this Agreement, return to the Disclosing Party all Confidential Information, including drawings, documents, reports and other tangible manifestations of Confidential Information received by the Receiving Party pursuant to this Agreement, together with all copies and reproductions thereof.",
            f"This Agreement shall be effective as of the Effective Date and shall terminate on the delivery of written notice of termination from either Party; provided, however, that the obligations of the Receiving Party under this Agreement shall remain in effect for a period of {self.data['confidentiality_period']} years from the date of termination.",
            f"This Agreement shall be governed and construed in accordance with the laws of India. The competent courts at {self.data['jurisdiction']} India shall have the sole and exclusive jurisdiction over any dispute that arises in relation to this Agreement.",
            "The Partner represents and covenants that its performance of this Agreement does not and will not breach any agreement it has entered into or will enter into with any third party. The Partner agrees not to enter into any written or oral agreement that conflicts with the provisions of this Agreement.",
            "The individuals executing this Agreement represent and warrant that they are empowered and duly authorized execute this Agreement on behalf of the parties they represent. Each Party represents and warrants to the other Party that it is authorised to execute this Agreement and is competent to discharge the obligations under this Agreement.",
            "Nothing in this Agreement will be construed to create a partnership, joint venture, franchise, fiduciary, employment or agency relationship between the parties. Neither Party has any express or implied authority to assume or create any obligations on behalf of the other or to bind the other to any contract, agreement or undertaking with any third party.",
            "If any provision of this Agreement shall be held by a court of competent jurisdiction to be illegal, invalid or unenforceable, the remaining provisions shall remain in full force and effect.",
            "This Agreement contains the full and complete understanding of the parties with respect to the subject matter hereof, and supersedes all prior representations and understandings, whether oral or written. This Agreement may be amended only in writing by mutual agreement of the Parties.",
        ]

        for i, clause in enumerate(clauses, 1):
            story.append(Paragraph(f"{i}. {clause}", self.styles["Justify"]))
            story.append(Spacer(1, 6))

    def add_signatures(self, story):
        story.append(
            Paragraph(
                "IN WITNESS WHEREOF, the parties have executed this Agreement under seal as of the Effective Date.",
                self.styles["Normal"],
            )
        )
        story.append(Spacer(1, 12))

        data = [
            ["Signature", "Name", "Designation", "Organisation"],
            ["", "", "", ""],
            ["", "", "", ""],
        ]
        t = Table(data, colWidths=[1.5 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch])
        t.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.25, colors.black),
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ]
            )
        )
        story.append(t)


# Usage example
json_data = """
{
    "effective_date": "September 27, 2024",
    "party1_name": "ABC Corporation",
    "party2_name": "XYZ Ltd.",
    "party1_business": "software development",
    "party2_business": "data analytics",
    "purpose": "exploring potential collaboration in AI-driven analytics",
    "confidentiality_period": "5",
    "jurisdiction": "Mumbai"
}
"""

# nda_generator = NDAGenerator(json_data)
# nda_generator.generate_pdf("nda_agreement.pdf")
