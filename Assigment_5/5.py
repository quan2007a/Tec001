def remove_odd(numbers):
    new_list = []

    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)

    return new_list


# Main program
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

result = remove_odd(my_list)

print("Original list:", my_list)
print("New list:", result)