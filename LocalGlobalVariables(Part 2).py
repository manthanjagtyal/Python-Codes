x=int(input("Enter number: "))
print(x)
def Hello():
    global x
    y=int(input("Enter any number to add it: "))
    x=x+y
Hello()
print("Here global variable changed inside a function by using global keyword:",x)
