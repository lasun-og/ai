rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"
actions = 0


def reflex_agent(room, status):
    if status == "Dirty":
        return "Suck"
    if room == "A":
        return "Move Right"
    return "Move Left"


print("AI-1: Vacuum Cleaner")
print("Starting rooms:", rooms)
while "Dirty" in rooms.values():
    status = rooms[location]
    action = reflex_agent(location, status)
    print("Room:", location, "|", status, "| Action:", action)
    actions += 1
    if action == "Suck":
        rooms[location] = "Clean"
    else:
        if location == "A":
            location = "B"
        else:
            location = "A"

print("Finished!")
print("Final rooms:", rooms)
print("Total actions:", actions)
