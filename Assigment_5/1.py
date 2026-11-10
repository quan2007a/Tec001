numbers = []

while True:
    number = input("Enter a number:")
    
    if number == "":
        break
    
    number = int(number)
    numbers.append(number)

    numbers.sort(reverse=True)

    print(numbers[:5])