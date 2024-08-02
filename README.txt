PDF Data Masking

Objective

The objective of this project is to develop a robust application that masks sensitive information from input PDFs, ensuring data privacy and security. 
The application handles both text and images within the PDF, accommodating diverse names across different demographics, including Malaysian, Chinese, and Korean names.

Features

Text Extraction and Masking:

Accurately extract text from PDF files.
Identify and mask sensitive information such as names, phone numbers, email addresses, and clinic names.
Support for names across different demographics, including Malaysian, Chinese, and Korean names.
Image Processing:

Extract text from images within the PDF using Optical Character Recognition (OCR).
Mask sensitive information found within these images.
Multi-language Support:

Ensure the solution can handle names in various languages and scripts, particularly non-English names.
Performance:

Efficient processing to handle large PDFs and multiple files simultaneously.
Ensure accuracy in identifying and masking sensitive information.

Defining the patterns for sensitive info detection:


Several regular expression patterns are defined to detect specific types of sensitive information:

Phone Numbers: The pattern r'\b\d{10}\b' detects sequences of exactly 10 digits (e.g., 1234567890).

Email Addresses: The pattern r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' matches typical email formats.

Credit Card Numbers: The pattern r'\b(?:\d[ -]*?){13,19}\b' identifies potential credit card numbers that may contain spaces or hyphens.

Social Security Numbers (SSN): The pattern r'\b\d{3}-\d{2}-\d{4}\b' looks for the standard SSN format.

Addresses: The pattern r'\b\d{1,5}\s\w+(\s\w+)+\b' detects addresses that typically start with a number followed by street names.

Names: The pattern r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b|\b[A-Z][A-Z]+\b(?:\s[A-Z][A-Z]+\b)?' captures full names formatted as "First Last" or all uppercase (e.g., "JOHN DOE").

Consecutive Numbers: The pattern r'\b\d{4,}\b' identifies sequences of 4 or more digits.


Technologies Used


Programming Language: Python
Libraries and Frameworks:
PyMuPDF (for PDF text and image extraction)
pytesseract (for OCR)
Pillow (for image manipulation)
OpenCV (for image processing)
spaCy (for Natural Language Processing)
pdfminer (for PDF text extraction)
re (for regular expressions)
reportlab (for creating output PDFs)
Setup

Install Required Libraries:

pip install PyMuPDF pytesseract Pillow opencv-python-headless spacy pdfminer.six reportlab

Download the spaCy model:

python -m spacy download en_core_web_sm

Ensure Tesseract OCR is installed and correctly configured.

File Structure

main.py
sensitive_info_detection.py
pdf_processing.py
image_processing.py
output_pdf.py
Algorithms and Code Explanation

main.py
This is the main script that coordinates the entire process of extracting, masking, and outputting the PDF content.

sensitive_info_detection.py
This file contains functions for detecting and masking sensitive information in text.

pdf_processing.py
This file contains functions for extracting text from PDF files.

image_processing.py
This file handles the extraction and OCR processing of images from PDF files.

output_pdf.py
This file contains the function for creating the output PDF with masked text.

Running the Application

Ensure you have an input.pdf file in your working directory.

Run the main.py script:

The processed output will be saved as output.pdf in the same directory.

Conclusion

This project provides a comprehensive solution for masking sensitive information in both text and images within PDF files. By leveraging various Python libraries and NLP techniques, it ensures accurate detection and masking of sensitive data while supporting multiple languages and scripts.






