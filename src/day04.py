import json
guest = {
    "name": "Miguel",
    "room": "101",
    "room_type": "double",
    "checked_in": True
    }

with open("guest.json", "w") as f:
    json.dump(guest, f, indent=2)

    print("Guest information saved to guest.json")

    # Exercise 2: Load guest from file
with open("guest.json") as f:
    loaded = json.load(f)

print(f"Name: {loaded['name']}")
print(f"Room: {loaded['room']}")
print(f"Checked in: {loaded['checked_in']}")

# Exercise 3: Save multiple guests
guests = [
    {"name": "Ana", "room": 101, "room_type": "single", "checked_in": True},
    {"name": "Carlos", "room": 102, "room_type": "double", "checked_in": True},
    {"name": "Laura", "room": 103, "room_type": "suite", "checked_in": False},
]

with open("guests.json", "w") as f:
    json.dump(guests, f, indent=2)

print("All guests saved ✓")

# Load and loop through them
with open("guests.json") as f:
    loaded_guests = json.load(f)

print("\n--- Guest List ---")
for guest in loaded_guests:
    status = "checked in" if guest["checked_in"] else "not checked in"
    print(f"Room {guest['room']}: {guest['name']} — {status}")

    # Exercise 4: Add a new guest to existing file
def add_guest(name, room, room_type):
    # Load existing guests
    with open("guests.json") as f:
        guests = json.load(f)
    
    # Add new guest
    new_guest = {
        "name": name,
        "room": room,
        "room_type": room_type,
        "checked_in": True
    }
    guests.append(new_guest)
    
    # Save back to file
    with open("guests.json", "w") as f:
        json.dump(guests, f, indent=2)
    
    print(f"{name} added to guests.json ✓")

# Test it
add_guest("Miguel", 104, "double")

# Confirm it's there
with open("guests.json") as f:
    all_guests = json.load(f)

print(f"\nTotal guests: {len(all_guests)}")
for guest in all_guests:
    print(f"  Room {guest['room']}: {guest['name']}")