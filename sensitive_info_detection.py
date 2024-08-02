import re
import spacy

nlp = spacy.load('en_core_web_sm')

def mask_sensitive_info(text):
    
    phone_number_pattern = r'\b\+?\d{10,15}\b'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    credit_card_pattern = r'\b(?:\d[ -]*?){13,19}\b'
    aadhar_pattern = r'\b\d{4}-\d{4}-\d{4}-\d{4}\b'
    address_pattern = r'\b\d{1,5}\s\w+([\s,]\w+)+\b'
    name_pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b|\b[A-Z][A-Z]+\b(?:\s[A-Z][A-Z]+\b)?'  
    consecutive_numbers_pattern = r'\b\d{4,}\b'  # Pattern for 4 or more consecutive numbers
    alphanumeric_pattern = r'\b(?=\w*[A-Za-z])(?=\w*\d)\w{7,}\b'

    def mask_pattern(pattern, text):
        return re.sub(pattern, lambda match: '*' * len(match.group(0)), text)

    text = mask_pattern(phone_number_pattern, text)
    text = mask_pattern(email_pattern, text)
    text = mask_pattern(credit_card_pattern, text)
    text = mask_pattern(aadhar_pattern, text)
    text = mask_pattern(address_pattern, text)
    text = mask_pattern(name_pattern, text)
    text = mask_pattern(consecutive_numbers_pattern, text)
    text = mask_pattern(alphanumeric_pattern, text)  

    doc = nlp(text)
    masked_text = []
    last_end = 0

    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'ORG']:
            masked_text.append(text[last_end:ent.start_char])
            masked_text.append('*' * (ent.end_char - ent.start_char))
            last_end = ent.end_char
        else:
            masked_text.append(text[last_end:ent.start_char])
            masked_text.append(text[ent.start_char:ent.end_char]) 
            last_end = ent.end_char

    masked_text.append(text[last_end:])
    return ''.join(masked_text)

