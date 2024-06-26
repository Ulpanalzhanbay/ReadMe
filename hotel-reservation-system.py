import datetime
from tabulate import tabulate
from abc import ABC, abstractmethod

class Accommodation(ABC):
    """Base class representing accommodation entities."""

    def __init__(self, room_number, capacity, price_per_night):
        """Initialize an Accommodation object with the given attributes."""
        self._room_number = room_number  # Encapsulation: Room number is now protected
        self._capacity = capacity  # Encapsulation: Capacity is now protected
        self._price_per_night = price_per_night  # Encapsulation: Price per night is now protected
        self._is_reserved = False  # Encapsulation: is_reserved is now protected
        self._reservation = None  # Encapsulation: Reservation is now protected

    @property
    def room_number(self):
        return self._room_number

    @property
    def capacity(self):
        return self._capacity

    @property
    def price_per_night(self):
        return self._price_per_night

    @property
    def is_reserved(self):
        return self._is_reserved

    @property
    def reservation(self):
        return self._reservation

    @abstractmethod
    def reserve(self, reservation):
        pass

    @abstractmethod
    def cancel_reservation(self):
        pass

class Room(Accommodation):
    """Class representing a hotel room."""

    def __init__(self, room_number, capacity, price_per_night):
        """Initialize a Room object with the given attributes."""
        super().__init__(room_number, capacity, price_per_night)

    def reserve(self, reservation):
        """Reserve the room with the provided reservation.

        Args:
            reservation (Reservation): The reservation to be associated with the room.

        Returns:
            bool: True if the reservation was successful, False otherwise.
        """
        if not self._is_reserved:
            self._is_reserved = True
            self._reservation = reservation
            return True
        else:
            return False

    def cancel_reservation(self):
        """Cancel the reservation associated with the room.

        Returns:
            bool: True if the reservation was canceled successfully, False otherwise.
        """
        if self._is_reserved:
            self._is_reserved = False
            self._reservation = None
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
        """Initialize a Hotel object with the given attributes."""
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

class Reservation(Accommodation):
    """Class representing a reservation."""

    def __init__(self, guest_name, room, check_in_date, check_out_date):
        """Initialize a Reservation object with the given attributes."""
        super().__init__(room.room_number, room.capacity, room.price_per_night)
        self._guest_name = guest_name  # Encapsulation: Guest name is now protected
        self._check_in_date = check_in_date  # Encapsulation: Check-in date is now protected
        self._check_out_date = check_out_date  # Encapsulation: Check-out date is now protected

    @property
    def guest_name(self):
        return self._guest_name

    @property
    def check_in_date(self):
        return self._check_in_date

    @property
    def check_out_date(self):
        return self._check_out_date

    def total_cost(self):
        """Calculate the total cost of the reservation.

        Returns:
            float: The total cost of the reservation.
        """
        nights = (self._check_out_date - self._check_in_date).days
        return nights * self._price_per_night

    def reserve(self, reservation):
        """Reserve the accommodation with the provided reservation."""
        # Specific implementation to reserve the accommodation

    def cancel_reservation(self):
        """Cancel the reservation."""
        # Specific implementation to cancel the reservation

def print_accommodation_info(accommodation):
    """Print information about an accommodation, including reservation details if any.

    Args:
        accommodation (Accommodation): The accommodation to display information about.
    """
    reservation_details = []
    if accommodation.is_reserved:
        reservation = accommodation.reservation
        reservation_details.append([reservation.guest_name, reservation.check_in_date, reservation.check_out_date])
    accommodation_data = [[accommodation.room_number, accommodation.capacity, f"${accommodation.price_per_night}", "Yes" if accommodation.is_reserved else "No"]]
    print(tabulate(accommodation_data, headers=["Room Number", "Capacity", "Price per Night", "Is Reserved"], tablefmt="pretty"))
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
    """Main function to run the hotel reservation system."""
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
                print_accommodation_info(room)
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
