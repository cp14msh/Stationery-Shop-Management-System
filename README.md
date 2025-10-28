# 🏪 Stationery Shop Management System

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is a simple, command-line interface (CLI) based shop management system written in Python. It allows a shop owner to manage product inventory, process sales, and view daily reports.

---

## 🚀 Features

* **Product Management:** Add new products or update the inventory stock for existing ones.
* **Sales Processing:** Process customer sales, automatically deducting the quantity from the inventory.
* **Inventory Check:** Quickly query the available stock for any given product.
* **Reporting:**
    * Calculate the total revenue (sales) for the day.
    * Calculate the total profit for the day.
* **Sales Analysis:** Identify the top-selling product of the day based on quantity sold.
* **Clean UI:** A clean, menu-driven user interface for easy navigation.

---

## 🛠 Requirements

* [Python 3.x](https://www.python.org/downloads/)

This project uses only the Python standard library and requires no external packages.

---

## ⚙️ How to Run

1.  Clone the repository or download the project files.
2.  Ensure your file structure matches the following:
    ```
    shop-project/
    ├── shop.py         # Contains the main class and business logic
    ├── main.py         # Contains the UI and main application loop
    └── README.md
    ```
3.  Open your terminal or command prompt and navigate to the project directory:
    ```bash
    cd path/to/shop-project
    ```
4.  Run the main application:
    ```bash
    python main.py
    ```
5.  Use the on-screen menu to select your desired options.

---

## 📈 Future Improvements

* **Data Persistence:** Implement a database (like SQLite) or file storage (JSON/CSV) to save inventory and sales data permanently.
* **Robust Error Handling:** Add more advanced input validation (e.g., prevent negative prices or quantities).
* **Graphical User Interface (GUI):** Rebuild the application with a GUI framework such as `Tkinter` or `PyQt`.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file (if one exists) for details.
