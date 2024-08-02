from sensitive_info_detection import mask_sensitive_info
from pdf_processing import extract_pdf_text
from output_pdf import create_output_pdf
from image_processing import extract_images_from_pdf, extract_text_from_image
import spacy

nlp = spacy.load('en_core_web_sm')

def process_pdf(pdf_path, output_path):
    text = extract_pdf_text(pdf_path)
    
    images = extract_images_from_pdf(pdf_path)
    image_texts = []
    for image in images:
        image_text = extract_text_from_image(image)
        image_texts.append(image_text)
    
    combined_text = text + "\n" + "\n".join(image_texts)
    
    masked_text = mask_sensitive_info(combined_text)
    
    create_output_pdf(masked_text, output_path)

if __name__ == '__main__':
    process_pdf('input.pdf', 'output.pdf')
