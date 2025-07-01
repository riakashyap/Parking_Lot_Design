# Parking Lot Design
An object-oriented parking lot management system built in Python.

This project simulates an automated parking lot system that can accommodate up to n cars at any given time. Each parking slot is assigned a number starting from 1, increasing with distance from the entry gate. The objective is to automate the ticketing and parking allocation process without human involvement.

## When a vehicle arrives, the system should:

-> Record the car's registration number and colour.

-> Assign the nearest available parking slot.

-> Issue a virtual ticket indicating the allocated slot.

-> When the car exits, the system marks the corresponding slot as available again.

## In addition to handling basic operations, the system must comply with regulatory requirements to support the following queries:

-> Get registration numbers of all cars with a specific colour.

-> Get the slot number for a car with a specific registration number.

-> Get all slot numbers occupied by cars of a given colour.

## => Features
1) Create a parking lot with a fixed capacity
2) Park cars with registration number and colour
3) Allocate the nearest available slot
4) Free up slots when cars leave

## => Query:
1) Slot numbers by car colour
2) Registration numbers by colour
3) Slot number by registration number
4) Print the current parking status

## Folder Structure 
```plaintext
parking-lot/
├── parking_lot.py        # Main Python file with ParkingLot and Car classes
└── README.md             # Project documentation
```

## How to Run
<pre>python parking_lot.py</pre>

