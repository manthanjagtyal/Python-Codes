marks=[10,12,3,41,52,35]
index=0
for mark in marks:
    print(mark)
    if (index==3):
        print(index,"Manthan is Awesome")
    index+=1
#its shortcut is enumurate function:
for index,mark in enumerate(marks):
    print(mark)
    if (index==3):
        print(index,"Manthan is Awesome")
