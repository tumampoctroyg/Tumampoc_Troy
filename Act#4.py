# Find the number closest to 300
goal = 300

def find_nearest(num_list):
    return min(num_list, key=lambda x: abs(x - goal))

def start_program():
    print(f"Target number is {goal}\n")

    while True:
        try:
            n1 = int(input("--- Enter your 1st number: ---\n"))
            n2 = int(input("--- Enter your 2nd number: ---\n"))
            n3 = int(input("--- Enter your 3rd number: ---\n"))

            num_list = [n1, n2, n3]

            closest = find_nearest(num_list)

            print(f"\nClosest number to {goal} is: {closest}")

            if input("\nTry again? (y/n): ").lower() != 'y':
                break

        except ValueError:
            print("\nError: Enter whole numbers only. Let's restart.\n")

start_program()
          
       
       
