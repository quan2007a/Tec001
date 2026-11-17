seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter a month (1-12): "))

if month >= 1 and month <= 12:
    season = seasons[((month + 2) // 3) % 4]
    print("The season is:", season)
else:
    print("Invalid month")