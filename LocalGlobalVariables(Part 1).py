x=input()
#Here this x is global variable because it can be used anywhere in the function
print()
def hello():
    y=input()
    print(y)
hello()
print("Now i will try to print y")
try:
    print(y) # pyright: ignore[reportUndefinedVariable]
except:
    print("I had tried to print y but i got error.Because y was an local variable which can be used only inside the function")
print(x)
