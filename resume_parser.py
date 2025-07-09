import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    data = {}

    # Very basic info extraction (customize based on resume format)
    name_match = re.search(r"Name[:\- ]*(.*)", text, re.IGNORECASE)
    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    phone_match = re.search(r"\+?\d[\d\s\-]{8,}", text)

    data["Name"] = name_match.group(1).strip() if name_match else "Not found"
    data["Email"] = email_match.group(0).strip() if email_match else "Not found"
    data["Phone"] = phone_match.group(0).strip() if phone_match else "Not found"

    # Add more fields as needed (skills, education, etc.)
    return data
