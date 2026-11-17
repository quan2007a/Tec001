text = "python is easy , python is fun , i love python."

def word_frequency(text, target_word):
    words = text.split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    return frequency.get(target_word.lower(), 0)


# text = "python is easy , python is fun , i love python."

print(word_frequency(text, "Python"))
print(word_frequency(text, "is"))
print(word_frequency(text, "Java"))
