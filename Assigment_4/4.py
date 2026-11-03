import re

def hide_phone(text):
    pattern = r"\+84\d{9}|\b\d{10}\b"

    result = re.sub(pattern, "[REDACTED]", text)

    return result


text = "My phone number is 0912345678 and +84912345678"

print(hide_phone(text))