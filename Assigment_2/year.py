year = int(input("enter a year:"))
def Leap_year(year):
    if year % 4 == 0:
        print("True")
    elif year % 100 == 0:
        print("True")
    elif year % 400 == 0:
         print("True")
    else:
        print("False")

Leap_year(year)