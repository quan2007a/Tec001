def acronym(phrase):
    words = phrase.split()
    result = ""

    for word in words:
        result = result + word[0].upper()

    return result

print(acronym("unidentified foreign object"))
print(acronym("as soon as possible"))
print(acronym("central processing unit"))