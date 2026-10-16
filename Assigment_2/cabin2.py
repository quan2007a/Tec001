cabin = input("Enter the cabin class:")
def Cabin_class(cabin):
    if cabin == "LUX":
        return "upper-deck cabin with a balcony"
    elif cabin == "A":
        return "above the car deck, equipped with a window"
    elif cabin == "B":
        return "windowless cabin above the car deck"
    elif cabin == "C":
        return "windowless cabin below the car deck"
    else:
        return "Invalid cabin class"        

print(Cabin_class(cabin))