## Hotel Reservation System

This is a simple hotel reservation system implemented in Python. It allows users to view room information, make reservations, and cancel reservations.

### Classes

#### Accommodation (Abstract Base Class)

- Base class representing accommodation entities.
- Attributes:
  - `room_number`: Room number.
  - `capacity`: Maximum capacity of the room.
  - `price_per_night`: Price per night for the room.
  - `is_reserved`: Boolean indicating if the room is reserved.
  - `reservation`: Reservation associated with the room.
- Methods:
  - `reserve(reservation)`: Abstract method to reserve the accommodation.
  - `cancel_reservation()`: Abstract method to cancel the reservation.

#### Room

- Represents a hotel room.
- Inherits from Accommodation.
- Methods:
  - `reserve(reservation)`: Reserves the room with the provided reservation.
  - `cancel_reservation()`: Cancels the reservation associated with the room.

#### Hotel

- Represents a hotel.
- Attributes:
  - `name`: The name of the hotel.
  - `rooms`: List of Room objects representing the rooms in the hotel.
- Methods:
  - `find_available_rooms(capacity, price_per_night)`: Finds available rooms based on capacity and maximum price per night.

#### Reservation

- Represents a reservation.
- Inherits from Accommodation.
- Methods:
  - `total_cost()`: Calculates the total cost of the reservation.

### Functions

- `print_accommodation_info(accommodation)`: Prints information about an accommodation, including reservation details if any.
- `print_available_rooms(available_rooms)`: Prints information about available rooms.

### Usage

1. Run the script.
2. Choose options from the menu:
   - View Room Information
   - Make a Reservation
   - Cancel Reservation
   - Exit

### Dependencies

- `datetime`: Used for date and time operations.
- `tabulate`: Used for generating formatted tables.
- `abc`: Used for defining abstract base classes and abstract methods.
