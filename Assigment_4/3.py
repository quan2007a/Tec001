import re

def sum_numbers(text):
    numbers = re.findall(r"\d+", text)

    total = 0

    for num in numbers:
        total = total + int(num)

    return total


paragraph = "Today is January 16, 2025. The temperature is 11 degrees Celsius."

print(sum_numbers(paragraph))