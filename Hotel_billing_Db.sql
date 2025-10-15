-- --------------------------------------------------------
-- Database: hotel_booking_system
-- --------------------------------------------------------
CREATE DATABASE IF NOT EXISTS hotel_booking_system;
USE hotel_booking_system;

-- --------------------------------------------------------
-- Table: customers
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    contact VARCHAR(15),
    id_proof VARCHAR(50),
    address VARCHAR(255)
);

-- Sample customer data
INSERT INTO customers (name, gender, contact, id_proof, address) VALUES
('Rahul Sharma', 'Male', '9876543210', 'Aadhar-1234', 'Mumbai, India'),
('Sneha Patel', 'Female', '9988776655', 'Aadhar-2345', 'Pune, India'),
('Amit Verma', 'Male', '9876001234', 'Aadhar-3456', 'Delhi, India'),
('Priya Mehta', 'Female', '8899776655', 'Aadhar-4567', 'Surat, India'),
('Rohit Singh', 'Male', '7788990011', 'Aadhar-5678', 'Jaipur, India');

-- --------------------------------------------------------
-- Table: rooms
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS rooms (
    room_no INT PRIMARY KEY,
    room_type VARCHAR(50),
    price FLOAT,
    availability VARCHAR(10)
);

-- Sample room data
INSERT INTO rooms (room_no, room_type, price, availability) VALUES
(101, 'Single', 1500.00, 'Available'),
(102, 'Double', 2500.00, 'Available'),
(103, 'Deluxe', 4000.00, 'Booked'),
(104, 'Suite', 6000.00, 'Available'),
(105, 'Single', 1500.00, 'Booked'),
(106, 'Deluxe', 4000.00, 'Available');

-- --------------------------------------------------------
-- Table: bookings
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    room_no INT,
    checkin_date DATE,
    checkout_date DATE,
    total_amount FLOAT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (room_no) REFERENCES rooms(room_no)
);

-- Sample booking data
INSERT INTO bookings (customer_id, room_no, checkin_date, checkout_date, total_amount) VALUES
(1, 105, '2025-10-10', '2025-10-12', 3000.00),
(3, 103, '2025-10-09', '2025-10-15', 24000.00);
