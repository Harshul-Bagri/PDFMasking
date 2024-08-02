import subprocess
import sys

def install_packages():
    packages = [
        'pdfminer.six',
        'pillow',
        'opencv-python',
        'pytesseract',
        'spacy',
        'reportlab',
        'pandas'
    ]
    
    for package in packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    
    # Download spaCy language model
    subprocess.check_call([sys.executable, '-m', 'spacy', 'download', 'en_core_web_sm'])

if __name__ == '__main__':
    install_packages()
