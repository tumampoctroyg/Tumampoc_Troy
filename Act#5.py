def highest_number():
    a = int(input("Enter num 1 for A value: "))
    b = int(input("Enter num 2 for B value: "))
    c = int(input("Enter num 3 for C value: "))

    if a > b and a > c:
        print("A", a, "is the highest number")
    elif b > a and b > c:
        print("B", b, "is the highest number")
    elif c > a and c > b:
        print("C", c, "is the highest number")

    elif a == b and a > c:
        print("A and B are equal and highest:", a)
    elif a == c and a > b:
        print("A and C are equal and highest:", a)
    elif b == c and b > a:
        print("B and C are equal and highest:", b)

    elif a == b == c:
        print("All numbers are equal!")

highest_number()
