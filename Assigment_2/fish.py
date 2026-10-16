fish = int(input("Length of a zander (cm):"))
def Fisher(fish):
    if fish >= 42:
        print("Approval")
    else:
        missing = 42 - fish
        print("The program instructs to release the fish back into the lake.")
        print("The fish was" ,missing, "cm below the size limit.")

Fisher(fish)