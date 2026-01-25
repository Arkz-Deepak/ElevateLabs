import shutil as sh
def add(*a):
    sum = 0
    for i in a:
        sum+=i
    print("The sum is ",sum)
def sub(a,b):
    diff = a-b
    print("The difference is ",diff)
def multi(*a):
    prod = 1
    for i in a:
        prod*=i
    print("The product is ",prod)
def div(a,b):
    try:
        quotient = a/b
        print("The quotient is ",quotient)
    except Exception as e:
        print("Error Obtained!\n ",e)
def main(a):
    if a != 5:
        a1 = int(input("Enter the first number :"))
        a2 = int(input("Enter the second number :"))

    if a == 1:
        add(a1,a2)
    elif a == 2:
        sub(a1,a2)
    elif a == 3:
        multi(a1,a2)
    elif a == 4:
        div(a1,a2)
    else:
        a = 5
    
columns = sh.get_terminal_size().columns
print("SIMPLE CALCULATOR \n \n".center(columns))
print("CHOOSE YOUR OPTION AND ENTER CORRESPONDING DIGIT".center(columns))
a=99
while(a!=5):
    print("OPTIONS".center(columns),"1.ADD 2 NUMBER".center(columns),"2.SUBTRACT 2 NUMBER".center(columns),"3.MULTIPY  2 NUMBER".center(columns),"4.DIVIDE  2 NUMBER".center(columns),"5.Exit".center(columns))
    a = int(input())
    main(a)