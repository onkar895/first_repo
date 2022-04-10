ch = input("Enter any character\n")

if ch == 'R' or ch == "r":
    print("color is red")
elif ch == 'Y' or ch == 'y':
    print("color is yellow")
elif ch == 'O' or ch == 'o':
    print("color is orange")
else:
    print("color is not valid")

if ch.isupper():
    print("Correct")
else:
    print("Wrong")

if ch.islower():
    print("Correct")
else:
    print("Wrong")

if ch.isalpha():
    print("correct")
else:
    print("wrong")