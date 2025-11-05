try:
    l=[1,2,3,4,5]
    i=int(input("Enter a Number: "))
    print(l[i])
except:
    print("Maybe index is wrong!")
finally:
    print("Am finally Keyword and i will run at any cost even after  error and am useful in functions.")
    #finally function runs even after return in function.
def finallys(n):
    try:
        n=int(input("Enter any integer: "))
        return 1
    except:
        print("wrong")
    finally:
        print("Am printing even after return.")
    print("I cant run because return function gone back")
print(finallys(1))
