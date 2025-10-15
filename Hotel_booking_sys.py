# -----------------------------------------------
# Hotel Booking System in Python + Tkinter + MySQL
# -----------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkcalendar import DateEntry

# -------------------- Database Connection --------------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",          # <-- Change this
    "password": "RAHUL123",  # <-- Change this
    "database": "hotel_booking_system"
}

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# -------------------- Main Window --------------------
root = tk.Tk()
root.title("Hotel Booking System")
root.geometry("1000x600")
root.configure(bg="#f0f8ff")  # light blue background

style = ttk.Style()
style.theme_use('clam')

# ---------- Frames ----------
top_frame = tk.Frame(root, bg="#4682b4", height=80)
top_frame.pack(side="top", fill="x")

left_frame = tk.Frame(root, bg="#87cefa", width=250)
left_frame.pack(side="left", fill="y")

main_frame = tk.Frame(root, bg="#f0f8ff")
main_frame.pack(side="right", fill="both", expand=True)

# ---------- Top Frame ----------
title = tk.Label(top_frame, text="🏨 Hotel Booking System", font=("Helvetica", 24, "bold"), bg="#4682b4", fg="white")
title.pack(pady=20)

# ---------- Left Menu ----------
def show_customer_frame():
    clear_main_frame()
    customer_frame()

def show_booking_frame():
    clear_main_frame()
    booking_frame()

def show_view_frame():
    clear_main_frame()
    view_frame()

buttons = [
    ("Customer Management", show_customer_frame),
    ("Room Booking", show_booking_frame),
    ("View Bookings", show_view_frame),
]

for b_text, b_command in buttons:
    btn = tk.Button(left_frame, text=b_text, font=("Helvetica", 12, "bold"),
                    bg="#4682b4", fg="white", relief="flat", command=b_command)
    btn.pack(pady=20, fill="x", padx=10)

# ---------- Clear Main Frame ----------
def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# -------------------- Customer Management --------------------
def customer_frame():
    lbl = tk.Label(main_frame, text="Customer Management", font=("Helvetica", 18, "bold"), bg="#f0f8ff")
    lbl.pack(pady=10)

    # Form
    form_frame = tk.Frame(main_frame, bg="#f0f8ff")
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Name", bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_frame, text="Gender", bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(form_frame, text="Contact", bg="#f0f8ff").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(form_frame, text="ID Proof", bg="#f0f8ff").grid(row=3, column=0, padx=5, pady=5)
    tk.Label(form_frame, text="Address", bg="#f0f8ff").grid(row=4, column=0, padx=5, pady=5)

    name_var = tk.StringVar()
    gender_var = tk.StringVar()
    contact_var = tk.StringVar()
    id_var = tk.StringVar()
    address_var = tk.StringVar()

    name_entry = tk.Entry(form_frame, textvariable=name_var)
    gender_entry = ttk.Combobox(form_frame, textvariable=gender_var, values=["Male", "Female", "Other"], state="readonly")
    contact_entry = tk.Entry(form_frame, textvariable=contact_var)
    id_entry = tk.Entry(form_frame, textvariable=id_var)
    address_entry = tk.Entry(form_frame, textvariable=address_var)

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    gender_entry.grid(row=1, column=1, padx=5, pady=5)
    contact_entry.grid(row=2, column=1, padx=5, pady=5)
    id_entry.grid(row=3, column=1, padx=5, pady=5)
    address_entry.grid(row=4, column=1, padx=5, pady=5)

    # Buttons
    def add_customer():
        name = name_var.get()
        gender = gender_var.get()
        contact = contact_var.get()
        id_proof = id_var.get()
        address = address_var.get()

        if name == "" or contact == "":
            messagebox.showerror("Error", "Please enter required fields!")
            return

        sql = "INSERT INTO customers (name, gender, contact, id_proof, address) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, (name, gender, contact, id_proof, address))
        conn.commit()
        messagebox.showinfo("Success", "Customer added successfully!")
        load_customers()

    def delete_customer():
        selected = tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a customer to delete!")
            return
        values = tree.item(selected, "values")
        customer_id = values[0]
        cursor.execute("DELETE FROM customers WHERE customer_id=%s", (customer_id,))
        conn.commit()
        messagebox.showinfo("Deleted", "Customer deleted successfully!")
        load_customers()

    btn_frame = tk.Frame(main_frame, bg="#f0f8ff")
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Add Customer", bg="#4682b4", fg="white", command=add_customer).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="Delete Customer", bg="#dc143c", fg="white", command=delete_customer).grid(row=0, column=1, padx=10)

    # Table
    tree = ttk.Treeview(main_frame, columns=("ID", "Name", "Gender", "Contact", "ID Proof", "Address"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Gender", text="Gender")
    tree.heading("Contact", text="Contact")
    tree.heading("ID Proof", text="ID Proof")
    tree.heading("Address", text="Address")
    tree.pack(fill="both", expand=True)

    def load_customers():
        for i in tree.get_children():
            tree.delete(i)
        cursor.execute("SELECT * FROM customers")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)

    load_customers()

# -------------------- Room Booking --------------------
def booking_frame():
    lbl = tk.Label(main_frame, text="Room Booking", font=("Helvetica", 18, "bold"), bg="#f0f8ff")
    lbl.pack(pady=10)

    form_frame = tk.Frame(main_frame, bg="#f0f8ff")
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Customer ID", bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_frame, text="Room No", bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(form_frame, text="Check-in Date", bg="#f0f8ff").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(form_frame, text="Check-out Date", bg="#f0f8ff").grid(row=3, column=0, padx=5, pady=5)

    customer_id_var = tk.StringVar()
    room_no_var = tk.StringVar()
    checkin_var = tk.StringVar()
    checkout_var = tk.StringVar()

    customer_entry = tk.Entry(form_frame, textvariable=customer_id_var)
    room_entry = ttk.Combobox(form_frame, textvariable=room_no_var)
    checkin_entry = DateEntry(form_frame, textvariable=checkin_var, date_pattern="yyyy-mm-dd")
    checkout_entry = DateEntry(form_frame, textvariable=checkout_var, date_pattern="yyyy-mm-dd")

    customer_entry.grid(row=0, column=1, padx=5, pady=5)
    room_entry.grid(row=1, column=1, padx=5, pady=5)
    checkin_entry.grid(row=2, column=1, padx=5, pady=5)
    checkout_entry.grid(row=3, column=1, padx=5, pady=5)

    # Load available rooms
    def load_rooms():
        cursor.execute("SELECT room_no FROM rooms WHERE availability='Available'")
        rooms = [str(r[0]) for r in cursor.fetchall()]
        room_entry['values'] = rooms

    load_rooms()

    def book_room():
        customer_id = customer_id_var.get()
        room_no = room_no_var.get()
        checkin = checkin_var.get()
        checkout = checkout_var.get()

        if customer_id == "" or room_no == "":
            messagebox.showerror("Error", "Please fill required fields!")
            return

        # Get room price
        cursor.execute("SELECT price FROM rooms WHERE room_no=%s", (room_no,))
        price = cursor.fetchone()[0]

        # Calculate days stayed
        from datetime import datetime
        fmt = "%Y-%m-%d"
        days = (datetime.strptime(checkout, fmt) - datetime.strptime(checkin, fmt)).days
        if days <= 0:
            messagebox.showerror("Error", "Checkout date must be after check-in date")
            return

        total = price * days

        cursor.execute("INSERT INTO bookings (customer_id, room_no, checkin_date, checkout_date, total_amount) VALUES (%s,%s,%s,%s,%s)",
                       (customer_id, room_no, checkin, checkout, total))
        cursor.execute("UPDATE rooms SET availability='Booked' WHERE room_no=%s", (room_no,))
        conn.commit()
        messagebox.showinfo("Success", f"Room booked successfully! Total: ₹{total}")
        load_rooms()

    tk.Button(main_frame, text="Book Room", bg="#4682b4", fg="white", command=book_room).pack(pady=10)

# -------------------- View Bookings --------------------
def view_frame():
    lbl = tk.Label(main_frame, text="View Bookings", font=("Helvetica", 18, "bold"), bg="#f0f8ff")
    lbl.pack(pady=10)

    tree = ttk.Treeview(main_frame, columns=("Booking ID", "Customer", "Room No", "Check-in", "Check-out", "Amount"), show="headings")
    tree.heading("Booking ID", text="Booking ID")
    tree.heading("Customer", text="Customer")
    tree.heading("Room No", text="Room No")
    tree.heading("Check-in", text="Check-in")
    tree.heading("Check-out", text="Check-out")
    tree.heading("Amount", text="Amount")
    tree.pack(fill="both", expand=True)

    cursor.execute("""
        SELECT b.booking_id, c.name, b.room_no, b.checkin_date, b.checkout_date, b.total_amount
        FROM bookings b
        JOIN customers c ON b.customer_id=c.customer_id
    """)
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

# -------------------- Start GUI --------------------
show_customer_frame()
root.mainloop()
