# Exercise 2: Loop through hotel rooms
# Creates a list containing the numbers of the hotel rooms to check.
rooms = [101, 102, 103, 104, 105]
# Repeats the indented code once for each room number in the rooms list.
for room in rooms:
    # Displays the room number currently being checked.
    print(f"Checking room {room}...")

# Prints a separator line between the two examples.
print("---")

# With enumerate — index + value
# Loops through the rooms list while providing both each position and its value.
for i, room in enumerate(rooms):
    # Displays the human-readable room position and the room number.
    print(f"room {i+1} of {len(rooms)}: {room}")

# Exercise 3: Error handling
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Can't divide by zero."

print(divide(10, 2))  # Outputs: 5.0
print(divide(10, 0))  # Outputs: Error: Can't divide by zero


# Exercise 4: Hotel room checker
def check_room(room_number):
    available_rooms = [101, 102, 103, 104, 105]
    try:
        room= int(room_number)
        if room in available_rooms:
            return f"Room {room} is available."
        else:
            return f"Room {room} is not available."
    except ValueError:
        return "Error: room must be a number."

#test all cases:
print(check_room(101))  # Outputs: Room 101 is available.
print(check_room(106))  # Outputs: Room 106 is not available.
print(check_room("abc"))  # Outputs: Error: room must be a number.