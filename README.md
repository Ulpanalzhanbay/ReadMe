import datetime
from tabulate import tabulate

class Room:
    
"""Class representing a hotel room.
    Attributes:
        room_number (str): The room number.
        capacity (int): The capacity of the room.
        price_per_night (float): The price per night for the room.
        is_reserved (bool): Indicates whether the room is reserved or not.
        reservation (Reservation or None): The reservation associated with the room.
"""

    def __init__(self, room_number, capacity, price_per_night):
        
"""Initialize a Room object with the given attributes.
"""
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_reserved = False
        self.reservation = None

    def reserve(self, reservation):
"""Reserve the room with the provided reservation.
        Args:
            reservation (Reservation): The reservation to be associated with the room.
        Returns:
            bool: True if the reservation was successful, False otherwise.
"""
        if not self.is_reserved:
            self.is_reserved = True
            self.reservation = reservation
            return True
        else:
            return False

    def cancel_reservation(self):
"""Cancel the reservation associated with the room.
        Returns:
            bool: True if the reservation was canceled successfully, False otherwise.
"""
        if self.is_reserved:
            self.is_reserved = False
            self.reservation = None
            return True
        else:
            return False

class Hotel:
"""Class representing a hotel.
    Attributes:
        name (str): The name of the hotel.
        rooms (list): List of Room objects representing the rooms in the hotel.
"""

    def __init__(self, name, rooms):
"""Initialize a Hotel object with the given attributes.
"""
        self.name = name
        self.rooms = rooms

    def find_available_rooms(self, capacity, price_per_night):
"""Find available rooms based on capacity and maximum price per night.
        Args:
            capacity (int): Required capacity for the room.
            price_per_night (float): Maximum price per night for the room.
        Returns:
            list: List of available Room objects that meet the criteria.
"""
        available_rooms = []
        for room in self.rooms:
            if not room.is_reserved and room.capacity >= capacity and room.price_per_night <= price_per_night:
                available_rooms.append(room)
        return available_rooms

class Reservation:
"""Class representing a reservation.
    Attributes:
        guest_name (str): The name of the guest making the reservation.
        room (Room): The room reserved.
        check_in_date (datetime.date): The check-in date of the reservation.
        check_out_date (datetime.date): The check-out date of the reservation.
"""

    def __init__(self, guest_name, room, check_in_date, check_out_date):
"""Initialize a Reservation object with the given attributes.
"""
        self.guest_name = guest_name
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def total_cost(self):
"""Calculate the total cost of the reservation.
        Returns:
            float: The total cost of the reservation.
"""
        nights = (self.check_out_date - self.check_in_date).days
        return nights * self.room.price_per_night

def print_room_info(room):
"""Print information about a room, including reservation details if any.
    Args:
        room (Room): The room to display information about.
"""
    reservation_details = []
    if room.is_reserved:
        reservation = room.reservation
        reservation_details.append([reservation.guest_name, reservation.check_in_date, reservation.check_out_date])
    room_data = [[room.room_number, room.capacity, f"${room.price_per_night}", "Yes" if room.is_reserved else "No"]]
    print(tabulate(room_data, headers=["Room Number", "Capacity", "Price per Night", "Is Reserved"], tablefmt="pretty"))
    if reservation_details:
        print(tabulate(reservation_details, headers=["Guest Name", "Check-in Date", "Check-out Date"], tablefmt="pretty"))

def print_available_rooms(available_rooms):
"""Print information about available rooms.
    Args:
        available_rooms (list): List of Room objects representing available rooms.
"""
    room_data = [[room.room_number, room.capacity, f"${room.price_per_night}"] for room in available_rooms]
    print(tabulate(room_data, headers=["Room Number", "Capacity", "Price per Night"], tablefmt="pretty"))

def main():
"""Main function to run the hotel reservation system.
"""
    room1 = Room("101", 2, 100)
    room2 = Room("102", 3, 150)
    room3 = Room("103", 4, 200)
    hotel = Hotel("Example Hotel", [room1, room2, room3])

    while True:
        print("\nWelcome to the Hotel Reservation System")
        print("1. View Room Information")
        print("2. Make a Reservation")
        print("3. Cancel Reservation")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            for room in hotel.rooms:
                print("\nRoom Information:")
                print_room_info(room)
        elif choice == "2":
            try:
                capacity = int(input("Enter required capacity: "))
                max_price = float(input("Enter maximum price per night: "))
                available_rooms = hotel.find_available_rooms(capacity, max_price)
                if available_rooms:
                    print("Available Rooms:")
                    print_available_rooms(available_rooms)
                    room_choice = input("Enter room number to reserve: ")
                    selected_room = next((room for room in available_rooms if room.room_number == room_choice), None)
                    if selected_room:
                        guest_name = input("Enter guest name: ")
                        check_in_date = datetime.datetime.strptime(input("Enter check-in date (YYYY-MM-DD): "),
                                                                   "%Y-%m-%d").date()
                        check_out_date = datetime.datetime.strptime(input("Enter check-out date (YYYY-MM-DD): "),
                                                                    "%Y-%m-%d").date()
                        reservation = Reservation(guest_name, selected_room, check_in_date, check_out_date)
                        selected_room.reserve(reservation)
                        print(f"Reservation made successfully. Total cost: ${reservation.total_cost()}")
                    else:
                        print("Invalid room number. Please try again.")
                else:
                    print("No available rooms matching the criteria.")
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

        elif choice == "3":
            try:
                guest_name = input("Enter guest name: ")
                for room in hotel.rooms:
                    if room.is_reserved and room.reservation.guest_name == guest_name:
                        room.cancel_reservation()
                        print("Reservation canceled successfully.")
                        break
                else:
                    print("No reservation found for this guest.")
            except AttributeError:
                print("No reservation found for this guest.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
