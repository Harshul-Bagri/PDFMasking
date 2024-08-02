def mask_sensitive_info(text, sensitive_info):
    for info in sensitive_info:
        text = text.replace(info, '[MASKED]')
    return text
