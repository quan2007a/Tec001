import re
ce = input("Enter course code:")

def check_valid_course(ce):
    if re.search(r"^[A-Z][A-Z][A-Z][0-9][0-9][0-9]$, ce "):
        return True
    else:
        return False

print(check_valid_course(ce))