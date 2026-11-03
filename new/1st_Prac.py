
# Vacuum Cleaner Agent

A = input("Enter status of Room A (Clean/Dirty): ").capitalize()
B = input("Enter status of Room B (Clean/Dirty): ").capitalize()
location = input("Enter starting location (A/B): ").upper()

rooms = {"A": A, "B": B}

while rooms["A"] == "Dirty" or rooms["B"] == "Dirty":
    print("\nCurrent Location:", location)

    if rooms[location] == "Dirty":
        print("Action: Suck")
        rooms[location] = "Clean"

    elif location == "A":
        print("Action: Move Right")
        location = "B"

    else:
        print("Action: Move Left")
        location = "A"

print("\nFinal Room Status:", rooms)
print("Both rooms are clean!")
