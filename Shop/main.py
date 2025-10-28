from shop import shop_management
import os

shop = shop_management()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_and_return():
    input("\nPress Enter to return to the main menu...")


while True:
    clear_screen()
    print("*******************************************")
    print("🏪  Stationery Shop Management System  🏪")
    print("*******************************************")
    print("\n--- MAIN MENU ---")
    print("  [1] Add / Update Product")
    print("  [2] Process a Sale")
    print("  [3] Check Product Inventory")
    print("  [4] View Daily Sales Report")
    print("  [5] View Top-Selling Product")
    print("  [6] Exit")
    print("-------------------------------------------")
    
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        clear_screen()
        print("--- [Add / Update Product] ---")
        name = input("Enter product name: ")
        try:
            price = float(input(f"Enter price for {name} ($): "))
            profit = float(input(f"Enter profit for {name} ($): "))
            inventory = int(input(f"Enter inventory quantity for {name}: "))
            shop.add_product(name, price, profit, inventory)
        except ValueError:
            print("\nError: Price, profit, and inventory must be valid numbers.")
        pause_and_return()
            
    elif choice == "2":
        clear_screen()
        print("--- [Process a Sale] ---")
        name = input("Enter product name to sell: ")
        try:
            how_many = int(input(f"Enter quantity of {name} to sell: "))
            shop.sell_product(name, how_many)
        except ValueError:
            print("\nError: Quantity must be a valid number.")
        pause_and_return()

    elif choice == "3":
        clear_screen()
        print("--- [Check Product Inventory] ---")
        name = input("Enter product name to check: ")
        shop.inventory(name)
        pause_and_return()

    elif choice == "4":
        clear_screen()
        print("--- [Daily Sales Report] ---")
        shop.Report_of_the_day()
        pause_and_return()
        
    elif choice == "5":
        clear_screen()
        print("--- [Top-Selling Product] ---")
        shop.the_product_of_day()
        pause_and_return()

    elif choice == "6":
        print("\nExiting system. Goodbye!")
        exit()
        
    else:
        print(f"\nError: '{choice}' is not a valid option. Please choose from 1-6.")
        pause_and_return()