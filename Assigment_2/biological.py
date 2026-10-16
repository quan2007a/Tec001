sex = input("Enter biological sex (male/female):")
hl = int(input("Enter hemoglobin value (g/l):"))
def check_hemoglobin(sex, hl):
    if sex == "female":
        if hl < 117:
            print("The hemoglobin value is low")
        elif hl <= 155:
            print("The hemoglobin value is normal")
        else:
            print("The hemoglobin value is high")

    if sex == "male":
            if hl < 134:
                print("The hemoglobin value is low")
            elif hl <= 167:
                print("The hemoglobin value is normal")
            else:
                print("The hemoglobin value is high")
    

check_hemoglobin(sex, hl)