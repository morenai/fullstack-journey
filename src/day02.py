# Exercise 2: Loop through hotel rooms
# Create a list with the room numbers we want to review.
rooms = [101, 102, 103, 104, 105]

# Loop through each room and print a status message.
for room in rooms:
    print(f"Checking room {room}...")

# Print a separator line to distinguish between the examples.
print("---")

# With enumerate — index + value
# In this loop, we get both the position and the value of each item.
for i, room in enumerate(rooms):
    # i + 1 is used so the index is more user-friendly.
    print(f"room {i + 1} of {len(rooms)}: {room}")

# Exercise 3: Error handling
# This function handles a common error: dividing by zero.
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Can't divide by zero."

# Tests for the division function.
print(divide(10, 2))  # Expected: 5.0
print(divide(10, 0))  # Expected: Error: Can't divide by zero


# Exercise 4: Hotel room checker
# This function checks whether a room is available or not.
def check_room(room_number):
    available_rooms = [101, 102, 103, 104, 105]
    try:
        room = int(room_number)
        if room in available_rooms:
            return f"Room {room} is available."
        else:
            return f"Room {room} is not available."
    except ValueError:
        return "Error: room must be a number."

# Test several cases to verify the expected behavior.
print(check_room(101))  # Room 101 is available.
print(check_room(106))  # Room 106 is not available.
print(check_room("abc"))  # Error: room must be a number.