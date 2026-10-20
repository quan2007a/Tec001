def middle_character(text):
    middle = len(text) // 2

    if len(text) % 2 == 0:
        return text[middle - 1:middle + 1]
    else:
        return text[middle]

print(middle_character("HELLO"))
print(middle_character("PYTHON"))
print(middle_character("HI"))