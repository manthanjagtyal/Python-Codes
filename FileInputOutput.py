x=input("Which Operation you want to do in file handling?(open,write,append,trick,delete)")
x.lower()
if x=="open":
    f=open('myfile.txt','r')
    text=f.read()
    print(text)
    f.close()
elif x=="write":
#In write mode, old text gets deleted and new text is added
    f=open('myfile.txt','w')
    b=input("Enter the content you want to write: ")
    f.write()
    f.close()
elif x=="append":
  #In append mode data gets added without deleting old one.
    f=open('myfile.txt','a')
    a=input("Enter the content you want to add: ")
    f.write(a)
#2nd trick to open and append
elif x=="trick":
    with open('myfile.txt','a') as f:
        f.write("I am Writing This from a short trick")
    print("Now check your txt file it will be surely added!")
elif x=="delete":
    with open('myfile.txt','w') as f:
        f.write(" ")
    print("Check the Txt file. Text will be deleted for sure!")
