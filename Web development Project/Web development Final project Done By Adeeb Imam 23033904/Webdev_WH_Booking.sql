CREATE DATABASE WH_BOOKING;
USE WH_BOOKING;

CREATE TABLE Guests (
    Guest_ID INT PRIMARY KEY,
    Guest_FirstName VARCHAR(255),
    Guest_LastName VARCHAR(255),
    Guest_Email VARCHAR(255),
    Guest_Password VARCHAR(255)
);

INSERT INTO Guests (Guest_ID, Guest_FirstName, Guest_LastName, Guest_Email, Guest_Password)
VALUES
(101, 'John', 'Doe', 'john.doe@example.com', 'password1'),
(102, 'Jane', 'Smith', 'jane.smith@example.com', 'password2'),
(103, 'Alice', 'Johnson', 'alice.johnson@example.com', 'password3');

select*
from bookings;


CREATE TABLE Hotels (
    Hotel_ID INT PRIMARY KEY,
    Hotel_City VARCHAR(255),
    Hotel_Rooms INT,
    Hotel_notpeakseasonprice DECIMAL(10, 2),
    Hotel_peakseasonprice DECIMAL(10, 2)
);

INSERT INTO Hotels (Hotel_ID, Hotel_City, Hotel_Rooms, Hotel_peakseasonprice, Hotel_notpeakseasonprice)
VALUES
(101, 'Aberdeen', 90, 140.00, 70.00),
(102, 'Belfast', 80, 130.00, 70.00),
(103, 'Birmingham', 110, 150.00, 75.00),
(104, 'Bristol', 100, 140.00, 70.00),
(105, 'Cardiff', 90, 130.00, 70.00),
(106, 'Edinburgh', 120, 160.00, 80.00),
(107, 'Glasgow', 140, 150.00, 75.00),
(108, 'London', 160, 200.00, 100.00),
(109, 'Manchester', 150, 180.00, 90.00),
(110, 'New Castle', 90, 120.00, 70.00),
(111, 'Norwich', 90, 130.00, 70.00),
(112, 'Nottingham', 110, 130.00, 70.00),
(113, 'Oxford', 90, 180.00, 90.00),
(114, 'Plymouth', 80, 180.00, 90.00),
(115, 'Swansea', 70, 130.00, 70.00),
(116, 'Bournemouth', 90, 130.00, 70.00),
(117, 'Kent', 100, 140.00, 80.00);


CREATE TABLE Room_Types(
	Room_Type VARCHAR(255) PRIMARY KEY,
    Room_max_limit INT
);
INSERT INTO Room_Types (Room_Type, Room_max_limit)
VALUES
("Standard", 1),
("Double", 2),
("Family", 4);

select*
from room_types;

CREATE TABLE Bookings (
    Booking_ID INT PRIMARY KEY,
    Guest_ID INT,
    Hotel_ID INT,
    Booking_NoOfGuest INT,
    Booking_RoomsBooked INT,
    Booking_DateOfReservation DATE,
    Booking_CheckIn_Date DATE,
    Booking_CheckOut_Date DATE,
    Booking_Total_nights INT,
    Booking_TotalPrice DECIMAL(10, 2),
    Booking_currency VARCHAR(50),
    Booking_DiscountPrice VARCHAR(255),
    Booking_Peak_Season CHAR(1),
    Room_Type VARCHAR(255),
    FOREIGN KEY (Guest_ID) REFERENCES Guests(Guest_ID),
    FOREIGN KEY (Hotel_ID) REFERENCES Hotels(Hotel_ID),
    FOREIGN KEY (Room_Type) REFERENCES Room_Types(Room_Type)
);

INSERT INTO Bookings
(Booking_ID, Guest_ID, Hotel_ID, Booking_NoOfGuest, Booking_RoomsBooked, Booking_DateOfReservation, Booking_CheckIn_Date, Booking_CheckOut_Date, Booking_Total_nights, Booking_TotalPrice, Booking_currency, Booking_DiscountPrice, Booking_Peak_Season, Room_Type)
VALUES
(1, 101, 108, 1, 1, '2024-03-21', '2024-04-01', '2024-04-03', 2, 400, "Pounds", "None", "Y", "Standard"),
(2, 102, 104, 2, 1, '2024-03-21', '2024-05-21', '2024-05-31', 10, 1456, "Pounds", "20%", "Y", "Double"),
(3, 103, 109, 4, 1, '2024-03-21', '2024-03-23', '2024-03-27', 4, 540, "Pounds", "None", "N", "Family");

CREATE TABLE Hotel_Price_Changes (
    Change_ID INT PRIMARY KEY,
    Hotel_ID INT,
    Change_Date DATE,
    New_Price DECIMAL(10, 2),
    FOREIGN KEY (Hotel_ID) REFERENCES Hotels(Hotel_ID)
);

CREATE TABLE Hotel_Management (
    Action_ID INT PRIMARY KEY,
    Action_Type VARCHAR(50),
    Hotel_ID INT,
    Action_Date DATE,
    FOREIGN KEY (Hotel_ID) REFERENCES Hotels(Hotel_ID)
);

CREATE TABLE Reports (
    Report_ID INT PRIMARY KEY,
    Report_Name VARCHAR(255),
    Report_Type VARCHAR(255),
    Report_Data TEXT
);