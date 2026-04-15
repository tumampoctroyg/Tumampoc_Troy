def send_message():
    message = input("Enter your message: ")
    with open("message.txt", "a") as file:
        file.write(message + "\n")
    print("Message saved!")

def view_messages():
    try:
        with open("message.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("No messages yet.")
            else:
                print("\n--- Messages ---")
                print(content)
    except FileNotFoundError:
        print("No messages yet.")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Send Message")
        print("2. View Messages")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            send_message()
        elif choice == "2":
            view_messages()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()







