import time
a=int(input("Enter pin to see time!"))
if a==1234:
    print(time.ctime())
else:
    raise ValueError("You have entered a value greater than 10.")
