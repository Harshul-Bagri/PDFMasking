import fitz  
import cv2
import pytesseract
from PIL import Image
import numpy as np
import spacy
import io

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

nlp = spacy.load('en_core_web_sm')

def extract_images_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    images = []
    
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            images.append(image)
    
    return images

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text
