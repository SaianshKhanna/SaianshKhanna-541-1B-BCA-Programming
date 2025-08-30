def main(): # Creating a function to perform
    expenses = {}  # Dictionary to store category input by user
    total = 0

    while True: 
        print("\n|| ~ Personal Expense Tracker ~ ||")
        print("1. Add Expense")
        print("2. View Total Spent")
        print("3. View Per-Category Breakdown")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount spent: "))
                category = input("Enter category (e.g. Food, Travel, Shopping): ")

                # Adds amount to total
                total += amount

                # Adds to category
                if category in expenses:
                    expenses[category] += amount
                else:
                    expenses[category] = amount

                print(f"Added {amount} in {category}.")
            except ValueError:
                print("Invalid amount! Please enter a number.") # Checks for errors and if there is one, it replies VALUE_ERROR

        elif choice == "2":
            print(f"\nTotal Spent: {total}") # Prints out the total spent (including all categories)

        elif choice == "3":
            if not expenses:
                print("\nNo expenses recorded yet.")
            else:
                print("\nPer-Category Breakdown:") # Prints out catery wise spent in total
                for cat, amt in expenses.items():
                    print(f"   {cat}: {amt}")

        elif choice == "4":
            print("Exiting, Now... Goodbye!\nThank You!")
            break
        else:
            print("Invalid choice, Please try again.")

main()

