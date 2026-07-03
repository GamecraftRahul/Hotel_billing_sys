# 🏨 Hotel Billing & Booking System

A modern **Hotel Billing & Booking System** developed using **Python**, **CustomTkinter**, and **MySQL**. The application provides a user-friendly graphical interface for managing hotel bookings, customer information, room allocation, and billing operations efficiently.

This project was created to practice Python desktop application development, MySQL database integration, and real-world hotel management concepts.

---

# 📖 Overview

The Hotel Billing & Booking System simplifies the process of managing hotel reservations and customer billing. Staff can register guests, allocate rooms, calculate bills automatically, and maintain booking records through an intuitive graphical interface.

The application is ideal for learning CRUD operations, database management, and GUI development using Python.

---

# ✨ Features

- 🏨 Hotel room booking management
- 👤 Customer registration
- 🛏️ Room allocation
- 📅 Check-in and check-out management
- 💰 Automatic bill calculation
- 🧾 Generate customer bills
- 🔍 Search customer records
- ✏️ Update booking information
- ❌ Delete booking records
- 📋 Display all bookings
- 💾 Store data in MySQL database
- 🎨 Modern CustomTkinter graphical interface

---

# 🛠️ Technologies Used

- Python 3
- CustomTkinter
- MySQL
- mysql-connector-python

---

# 📂 Project Structure

```
Hotel_billing_sys/
│
├── Hotel_booking_sys.py      # Main Application
├── Hotel_billing_Db.sql      # Database Script
├── README.md                 # Project Documentation
```

---

# 🗄️ Database

The project uses a **MySQL** database to store:

- Customer Information
- Room Details
- Booking Records
- Billing Information

Import the provided SQL file before running the application.

```
Hotel_billing_Db.sql
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/hotel-billing-system.git
```

---

## 2. Navigate to the Project Folder

```bash
cd hotel-billing-system
```

---

## 3. Install Required Libraries

```bash
pip install customtkinter
pip install mysql-connector-python
```

---

## 4. Import the Database

Open MySQL Workbench (or any MySQL client) and import:

```
Hotel_billing_Db.sql
```

---

## 5. Configure Database Credentials

Open:

```
Hotel_booking_sys.py
```

Update your MySQL credentials:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "hotel_db"
}
```

---

## 6. Run the Application

```bash
python Hotel_booking_sys.py
```

---

# 🖥️ Application Workflow

1. Register customer details.
2. Select available room.
3. Enter booking information.
4. Calculate room charges automatically.
5. Generate customer bill.
6. Save booking details.
7. Search or update existing bookings.
8. Display booking history.

---

# 📋 Modules

### 👤 Customer Management

- Add Customer
- Update Customer
- Delete Customer
- Search Customer

### 🏨 Room Management

- Room Allocation
- Room Availability
- Room Information

### 💰 Billing System

- Automatic Bill Calculation
- Total Amount Generation
- Booking Summary

### 🗄️ Database

- Save Customer Records
- Store Booking Information
- Retrieve Previous Records

---

# 📚 Learning Objectives

This project demonstrates:

- Python Programming
- GUI Development using CustomTkinter
- MySQL Database Connectivity
- CRUD Operations
- Object-Oriented Programming
- Event Handling
- Hotel Management Logic
- Billing System Development

---

# 🚀 Future Improvements

- 🔐 Admin Login System
- 👥 Multi-user Support
- 🧾 PDF Bill Generation
- 🖨️ Receipt Printing
- 📊 Dashboard & Analytics
- 📅 Online Reservation System
- 💳 Online Payment Gateway
- 📧 Email Booking Confirmation
- ☁️ Cloud Database Integration
- 📱 Responsive Interface

---

# 📸 Screenshots

You can add screenshots here after uploading images.

```
Home Window

Customer Registration

Room Booking

Billing Window

Booking Records
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is developed for educational and learning purposes.

You are free to use, modify, and improve this project for personal and academic use.

---

# 👨‍💻 Author

**Rahul Kulkarni**

GitHub: https://github.com/GamecraftRahul

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the project
- 📢 Share it with others

---

# 💡 Project Highlights

- ✅ Modern CustomTkinter Interface
- ✅ MySQL Database Integration
- ✅ Hotel Booking Management
- ✅ Customer Record Management
- ✅ Automatic Billing
- ✅ Search & Update Functionality
- ✅ Beginner-Friendly Code Structure
- ✅ Real-world Hotel Management Project

---

## 🌟 Ideal For

- Python Beginners
- Database Management Learning
- GUI Application Development
- College Mini Projects
- Hotel Management System Practice

---

**Made with ❤️ using Python, CustomTkinter, and MySQL**
