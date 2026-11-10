n= int(input('Enter numbers: '))
prime_number=n>1
for i in range(2,(n ** 0.5) + 1):
    if n % i == 0:
        prime_number = False
        break 
if prime_number:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")