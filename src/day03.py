# Day 03 — Classes & OOP

class HotelRoom:
    def __init__(self, number, room_type):
        self.number = number
        self.room_type = room_type
        self.occupied = False
        self.guest = None

    def check_in(self, guest_name):
        if self.occupied:
            return f"Room {self.number} is already occupied"
        self.occupied = True
        self.guest = guest_name
        return f"{guest_name} checked into room {self.number}"

    def check_out(self):
        if not self.occupied:
            return f"Room {self.number} is already empty"
        self.guest = None
        self.occupied = False
        return f"Room {self.number} is now available"

    def status(self):
        if self.occupied:
            return f"Room {self.number} — occupied by {self.guest}"
        return f"Room {self.number} — available"

    def __repr__(self):
        status = "occupied" if self.occupied else "available"
        return f"HotelRoom({self.number}, {self.room_type}, {status})"

# Test single room
room = HotelRoom(101, "double")
print(room.status())
print(room.check_in("Miguel"))
print(room.status())
print(room.check_out())
print(room.status())

# Multiple rooms
hotel = [
    HotelRoom(101, "single"),
    HotelRoom(102, "double"),
    HotelRoom(103, "suite"),
    HotelRoom(104, "single"),
    HotelRoom(105, "double"),
]

hotel[0].check_in("Ana")
hotel[1].check_in("Carlos")
hotel[2].check_in("Miguel")

print("\n--- Hotel Status ---")
for room in hotel:
    print(room.status())

available = [r for r in hotel if not r.occupied]
print(f"\nAvailable rooms: {len(available)}")
print(f"Occupied rooms: {len(hotel) - len(available)}")

print("\n--- Room Objects ---")
for room in hotel:
    print(room)