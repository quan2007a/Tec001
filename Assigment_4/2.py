import re

def check_color(color):
    pattern = r"^#[0-9A-Fa-f]{6}$"

    if re.match(pattern, color):
        return True
    else:
        return False


print(check_color("#FF5733"))
print(check_color("#abc123"))
print(check_color("#GG1234"))