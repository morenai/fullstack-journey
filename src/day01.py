# --- Exercise: Hotel utilities ---
# This file contains utility functions for basic hotel logic.
# Each function solves a small task that can be reused in other parts of the program.

# Calculates the total cost of a reservation based on the nightly price and number of nights.
def calculate_total(price_per_night, nights):
    return price_per_night * nights

# Checks whether a room is available by comparing the received status with the expected value.
def is_available(room_status):
    return room_status == "available"

# Formats guest information to display the name and room number.
def format_guest(name, room):
    return f"Guest: {name} | Room {room}"

# Counts how many items are in the guest list.
def count_guests(guest_list):
    return len(guest_list)

# Returns a greeting based on the time of day.
def get_greeting(hour):
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# Tests the functions above to verify they work correctly.
print(calculate_total(120, 3))
print(is_available("available"))
print(is_available("occupied"))
print(format_guest("Miguel", 101))
print(count_guests(["Ana", "Carlos", "Luis"]))
print(get_greeting(9))
print(get_greeting(15))
print(get_greeting(20))