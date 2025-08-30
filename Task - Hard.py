class Item:

    def __init__(self, name, price, stock): 
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - Rs.{self.price} ({self.stock} left)"


class Vending_Machine:

    def __init__(self):
        # Premade - Inventory
        self.inventory = {
            1: Item("Coca Cola", 40, 5),
            2: Item("Chips", 30, 3),
            3: Item("Water", 20, 10),
            4: Item("Protein Bar", 50, 2),
            5: Item("Sandwiches", 70, 7),
            6: Item("Cup Noodles", 130, 6)
        }
        self.cart = []  # Stores items added by user
        self.user_balance = 0 

    # ---------------- USER SECTION ----------------
    def show_items(self):
        print("\nAvailable Items:")
        for index, item in self.inventory.items(): # Prints out the inventory
            print(f"{index}. {item}") 

    def add_to_cart(self, itemID):
        if itemID in self.inventory:
            item = self.inventory[itemID]
            if item.stock > 0: # Adds to cart if only the stock is not emptied
                self.cart.append(item)
                item.stock -= 1  # Reduces the inventory asap u add it to cart
                print(f"Added item, {item.name} to your cart!")
            else:
                print("Sorry, that item is out of stock!")
        else:
            print("Invalid item selected.")

    def view_cart(self): 
        if not self.cart: # Checks for empty cart 
            print("\nCart is empty.")
            return 0
        else:
            print("\nYour Cart:")
            total = 0 # If not empty, prints out the cart and its item
            for ind, item in enumerate(self.cart, start=1):
                print(f"{ind}. {item.name} - Rs.{item.price}")
                total += item.price
            print(f"Total: Rs.{total}")
            return total

    def insert_money(self, amount):   # Inserts money by user 
        if amount <= 0:
            print("Invalid amount! Please insert money.") 
            return
        self.user_balance += amount # Adds user money to a variable amount
        print(f"Inserted Rs.{amount}.")

    def checkout(self):
        cost = self.view_cart()
        if cost == 0:
            print("Add items.") # Suggests to add items cuz carts empty
            return
        elif self.user_balance >= cost:
            change = self.user_balance - cost  # Calculates change to provide back to user         
            print("\nDispensing Items:")
            for item in self.cart: # For Loop and checks out the cart
                print(f"- {item.name}") 
            print(f"Purchase successful! Change returned, Rs.{change}.")

            self.cart.clear()  # Empties out the cart.
            self.user_balance = 0
        else:
            print(f"Insufficient balance! Please insert at least Rs.{cost - self.user_balance} more.")

    # ---------------- ADMIN SECTION ---------------- 
    def admin_menu(self):
        password = input("Enter admin password: ")
        if password != "admin123":   # Simple password system for the owner of vending machine or restocker
            print("Incorrect password! Returning to main menu.")
            return

        while True:
            print("\n// ~ Admin Menu ~ \\")
            print("1. Restock Item")
            print("2. Add New Item")
            print("3. Back to Main Menu")

            choice = input("Enter your choice: ") # Printing out the Admin Menu.

            if choice == "1":
                self.show_items() # Shows the current inventory
                try:
                    itemID = int(input("Enter item number to restock: ")) 
                    qty = int(input("Enter quantity to add: ")) 
                    if itemID in self.inventory and qty > 0:   # Checks if admin isn't adding something of 0 quantity
                        self.inventory[itemID].stock += qty 
                        print(f"Restocked {self.inventory[itemID].name}, new stock: {self.inventory[itemID].stock}")
                    else:
                        print("Invalid input.")
                except ValueError: 
                    print("Please enter a valid number.")
 
            elif choice == "2":
                try:  # Adding new item and getting to know the price and stock 
                    new_id = max(self.inventory.keys()) + 1
                    name = input("Enter new item name: ")
                    price = int(input("Enter price: "))
                    stock = int(input("Enter stock: "))
                    if price > 0 and stock > 0: 
                        self.inventory[new_id] = Item(name, price, stock)
                        print(f"Added new item: {self.inventory[new_id]}")
                    else:
                        print("Price and stock must be positive!") # Checks for the value to be positive not 0 or negative
                except ValueError:
                    print("Invalid input.")

            elif choice == "3": 
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice, Please try again.")


    # ---------------- MAIN PROGRAM ----------------
def main():
    vm = Vending_Machine() 

    while True: # Getting everything together in a loop
        print("\n// ~~ Virtual Vending Machine ~~ //")
        print("1. View Items")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Insert Money")
        print("5. Checkout")
        print("6. Admin Section")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vm.show_items()
            
        elif choice == "2":
            vm.show_items()
            try:
                itemID = int(input("Enter item number to add: "))
                vm.add_to_cart(itemID)
            except ValueError:
                print("Invalid input! Please enter a number.")
                
        elif choice == "3":
            vm.view_cart()
            
        elif choice == "4":
            try:
                amount = int(input("Enter amount to insert: "))
                vm.insert_money(amount)  
            except ValueError:
                print("Invalid input! Enter a valid number.")
                
        elif choice == "5":
            vm.checkout()
            
        elif choice == "6":
            vm.admin_menu()
            
        elif choice == "7":
            print("Thanks for using the vending machine! Goodbye.")
            break
        else:
            print("Invalid choice, try again.")


main()

