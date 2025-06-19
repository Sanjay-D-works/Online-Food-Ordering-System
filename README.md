# Online-Food-Ordering-System
# 🍽️ Online Food Ordering System (Console-Based - Python)

A **console-based food ordering system** implemented using **Python** and **Object-Oriented Programming (OOP)** principles. This project simulates user login/registration, restaurant and food browsing, ordering, and payment — all within the terminal.

---

## 🔧 Technologies Used

- ✅ Python 3.x
- ✅ Object-Oriented Programming (OOP)
- ✅ Built-in modules (no third-party libraries used)
- ✅ Modular structure with packages and abstraction

---

## 🧠 Project Overview

This project allows users to:

- Register or log in
- Browse restaurants and menus
- Select food items and place an order
- Simulate payment and see a receipt

It supports:
- Registered users
- Guest login
- Cart-based food ordering
- Simple search functionality

---

## 📁 Project Folder Structure

OnlineFoodOrderingSystem/
├── main.py
├── FoodApp.py
├── Controller/
│ ├── FoodManager.py
│ └── MainMenu.py
├── Models/
│ ├── AbstractItem.py
│ ├── Cart.py
│ ├── FoodItem.py
│ ├── FoodMenu.py
│ ├── Restaurant.py
│ ├── User.py
│ └── UserManager.py
└── README.md


> 💡 `__init__.py` files should be added to `Models/` and `Controller/` directories to make them Python packages.

---

## ▶️ How to Run

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/OnlineFoodOrderingSystem.git
   cd OnlineFoodOrderingSystem

python3 main.py

Follow prompts on terminal to register, log in, and order food.

🚀 Features

👤 User Registration and Login
🎭 Guest Login Support
🏪 Browse and Search Restaurants
🍱 View Food Items and Menus
🛒 Add Items to Cart and Place Order
💳 Simulated Payment System (UPI, Card, COD)
✅ Follows OOP principles (abstraction, encapsulation, etc.)
📌 Future Improvements

🧾 Store user data using files or database (currently in-memory)
🔍 Implement search by food item
📱 Build GUI using Tkinter or migrate to Flask web app
🧪 Add unit testing with unittest
👨‍💻 Author

Sanjay D
📧 [Your email]
🌐 GitHub: https://github.com/Sanjay-D-works

📜 License

This project is licensed under the MIT License.