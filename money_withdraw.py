def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Please enter a valid amount.")
                continue

            if amount > balance:
                print("Insufficient funds!")

                print("\nWhat would you like to do?")
                print("1. Try again")
                print("2. Check balance")
                print("3. Exit")

                option = input("Enter choice: ")

                if option == "1":
                    continue
                elif option == "2":
                    print("Current balance:", balance)
                elif option == "3":
                    return balance
                else:
                    print("Invalid option.")

            else:
                balance -= amount
                print("Withdrawal successful!")
                print("Remaining balance:", balance)
                return balance

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    balance = 1000.0  # starting balance

    while True:
        try:
            print("\n=== MENU ===")
            print("1. Withdraw")
            print("2. Check Balance")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                balance = withdraw(balance)

            elif choice == "2":
                print("Current balance:", balance)

            elif choice == "3":
                print("Thank you for using the system!")
                break

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print("Unexpected error:", e)


# Run the program
main()