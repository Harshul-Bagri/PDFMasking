from pdfminer.high_level import extract_text

def extract_pdf_text(pdf_path):
    text = extract_text(pdf_path)
    return text
