# --- Exercise: Hotel utilities ---

def calculate_total(price_per_night, nights):
    return price_per_night * nights
    
def is_available(room_status):
    return room_status == "available"

def format_guest(name, room):
    return F"Guest: {name} | Room {room}"

def count_guests(guest_list):
    return len(guest_list)

def get_greeting(hour):
    if hour <12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

#testing all of them.
print(calculate_total(120, 3))
print(is_available("available"))
print(is_available("occupied"))
print(format_guest("Miguel", 101))
print(count_guests(["Ana", "Carlos", "Luis"]))
print(get_greeting(9))
print(get_greeting(15))
print(get_greeting(20))