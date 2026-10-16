import math

def unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * radius ** 2
    area_m2 = area / 10000
    unit = price / area_m2
    return unit

diameter1 = float(input("Enter diameter of pizza 1 (cm): "))
price1 = float(input("Enter price of pizza 1 (USD): "))

diameter2 = float(input("Enter diameter of pizza 2 (cm): "))
price2 = float(input("Enter price of pizza 2 (USD): "))

unit1 = unit_price(diameter1, price1)
unit2 = unit_price(diameter2, price2)

print("Pizza 1 unit price:", round(unit1, 2), "USD per m2")
print("Pizza 2 unit price:", round(unit2, 2), "USD per m2")

if unit1 < unit2:
    print("Pizza 1 provides better value for money.")
elif unit2 < unit1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")