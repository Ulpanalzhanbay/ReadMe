# Hotel Reservation System

This Python program implements a simple hotel reservation system. It allows users to view room information, make reservations, cancel reservations, and exit the system.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview

This hotel reservation system consists of the following classes:

- **Room**: Represents a hotel room with attributes such as room number, capacity, price per night, reservation status, and associated reservation details.
- **Hotel**: Represents a hotel with a name and a list of rooms. It provides a method to find available rooms based on capacity and maximum price per night.
- **Reservation**: Represents a reservation with details such as guest name, reserved room, check-in date, and check-out date.
- **Main**: Contains the main function to run the hotel reservation system, which interacts with users through a command-line interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ulpanalzhanbay/hotel-reservation-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hotel-reservation-system
   ```
3. Install dependencies:
   ```bash
   pip install tabulate
   ```

## Usage

To run the hotel reservation system, execute the main Python script:
```bash
python main.py
```

Follow the prompts to perform the following actions:
1. View Room Information
2. Make a Reservation
3. Cancel Reservation
4. Exit

## Contributing

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md) to contribute to this project.
