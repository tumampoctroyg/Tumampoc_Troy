
while True:
    getInput = input("Input password: ")
    hasNum = False
    hasLetter = False
    
    for l in list(getInput):
        if l.isalpha():
            hasLetter = True
        if l.isdigit():
            hasNum = True
    
    if hasLetter and hasNum:
        print("Password accepted.")
        break
    else:
        print("Invalid password. Try again.")
