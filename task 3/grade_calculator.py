print("Starting grade calculator")
mark = int(input("Enter your mark of subject : "))
if mark>95 and mark<=100:
    print("Congratulations! You got a A+!")

elif mark>89 and mark<=95:
    print("Congratulations! You got a A!")

elif mark>83 and mark<=89:
    print("Congratulations! You got a B+!")

elif mark>75 and mark<=83:
    print("Congratulations! You got a B!")

elif mark>68 and mark<=75:
    print("You got a C+!")

elif mark>60 and mark<=68:
    print("You got a C!")
elif mark<60:
    print("Sorry You got F")
else:
    print("Enter a valid mark!")