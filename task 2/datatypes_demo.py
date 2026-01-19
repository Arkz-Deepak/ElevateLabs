a = int(5) # Declaring a integer
b = float(6) # Declaring a float value
c = bool(0) # Declaring a boolean value
d = str("oichsf51684 <= This is string") #Declaring a string

print(a," is of the type ",type(a))
print(b," is of the type ",type(b))
print(c," is of the type ",type(c))
print(d," is of the type ",type(d))
# Printing the tpes of the variables

sum = a + b
diff = a - b
mul = a * b
div = a / b
# Doing the arithmatic operation 

print(f"""Sum = {sum}
Difference = {diff}
Multiplication = {mul}
Division = {div}""")
# Printing the answers of arithmetic operations

string_integer = ord(input("Enter a character :"))
string_float = float(string_integer)

print("The integer form ",chr(string_integer)," is ",string_integer)
print("The float form ",chr(string_integer)," is ",string_float)

try:
    a = int(input("Enter a name:"))
    print("Hi ",a)
except Exception  as e:
    print("Error in last command:\n",e)
# handing the input if there is any error