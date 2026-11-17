numbers = []

while True:
    number = input("Enter a number (press Enter to quit): ")

    if number == "":
        break

    numbers.append(int(number))

numbers.sort(reverse=True)

print("The five greatest numbers are:")

for i in range(5):
    if i < len(numbers):
        print(numbers[i])