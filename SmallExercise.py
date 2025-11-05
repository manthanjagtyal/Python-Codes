x=input("Enter the thing you want to write in coding: ")
def code(x):
    
    if len(x)==0:
        return ""
    else:
        return code(x[1:])+x[0]
print("\n",code(x))
z=code(x)
y=input("\nYou want to decode it then\nEnter Password: ")
if y=="Manthan" or y=="manthan" or y=="MANTHAN":
    def decode(z):
        if len(z)==0:
            return ""
        else:
            return decode(z[1:])+z[0]
    print(f"{decode(z)}\n")
else:
    print("Wrong Password")
