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
        self.cart = []  # stores items added by user
        self.user_balance = 0 

    # ---------------- USER SECTION ----------------
    def show_items(self):
        print("\nAvailable Items:")
        for index, item in self.inventory.items():
            print(f"{index}. {item}")

    def add_to_cart(self, itemID):
        if itemID in self.inventory:
            item = self.inventory[itemID]
            if item.stock > 0:
                self.cart.append(item)
                item.stock -= 1
                print(f"Added item, {item.name} to your cart!")
            else:
                print("Sorry, that item is out of stock!")
        else:
            print("Invalid item selected.")

    def view_cart(self):
        if not self.cart:
            print("\nCart is empty.")
            return 0
        else:
            print("\nYour Cart:")
            total = 0
            for ind, item in enumerate(self.cart, start=1):
                print(f"{ind}. {item.name} - ₹{item.price}")
                total += item.price
            print(f"Total: ₹{total}")
            return total

    def insert_money(self, amount):   
        if amount <= 0:
            print("Invalid amount! Please insert money.")
            return
        self.user_balance += amount
        print(f"Inserted Rs.{amount}.")

    def checkout(self):
        cost = self.view_cart()
        if cost == 0:
            print("Add items.")
            return
        elif self.user_balance >= cost:
            change = self.user_balance - cost   
            print("\nDispensing Items:")
            for item in self.cart:
                print(f"- {item.name}")
            print(f"Purchase successful! Change returned, Rs.{change}.")

            self.cart.clear()  # Empties out the cart.
            self.user_balance = 0
        else:
            print(f"Insufficient balance! Please insert at least Rs.{cost - self.user_balance} more.")

    # ---------------- ADMIN SECTION ----------------
    def admin_menu(self):
        password = input("Enter admin password: ")
        if password != "admin123":   # simple password system
            print("Incorrect password! Returning to main menu.")
            return

        while True:
            print("\n// ~ Admin Menu ~ \\")
            print("1. Restock Item")
            print("2. Add New Item")
            print("3. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_items()
                try:
                    itemID = int(input("Enter item number to restock: "))
                    qty = int(input("Enter quantity to add: "))
                    if itemID in self.inventory and qty > 0:
                        self.inventory[itemID].stock += qty
                        print(f"Restocked {self.inventory[itemID].name}, new stock: {self.inventory[itemID].stock}")
                    else:
                        print("Invalid input.")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "2":
                try:
                    new_id = max(self.inventory.keys()) + 1
                    name = input("Enter new item name: ")
                    price = int(input("Enter price: "))
                    stock = int(input("Enter stock: "))
                    if price > 0 and stock > 0:
                        self.inventory[new_id] = Item(name, price, stock)
                        print(f"Added new item: {self.inventory[new_id]}")
                    else:
                        print("Price and stock must be positive!")
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

    while True:
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
