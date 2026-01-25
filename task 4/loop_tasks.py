print("Counter to 100 started!")
for i in range(100):
    print(i+1)
a = int(input("Enter the number to count upto : "))
while(a>=0):
    print(f"Count {a}")
    a-=1
print("Counter Completed!")
a = int(input("Enter the number to count(within 20 and only odd number is counted!) : "))
while(a>=0):
    if a>20: print("Error over the limit"); break
    if a%2==0: a-=1; continue
    print(f"Count {a}")
    a-=1
a = input("Enter any long word you know : ")
for i in a:
    print(i)
print("Tables of 5 is given below")
for i in range(1,11,1):
    print(f"5 X {i} = {5*i}")
print("printing even number till 10")
for i in range(0,11,2):
    print(i)

