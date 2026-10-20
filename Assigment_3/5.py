correct_username = "Quan"
correct_password = "123"

attempts = 0

while attempts < 5:
    username = input("Enter username:")
    password = input("Enter password:")

    if username == correct_username and password == correct_password:
        print("Welcome, Quan!!!")
        break
    else:
        attempts = attempts + 1

if attempts == 5:
    print("Access denied")