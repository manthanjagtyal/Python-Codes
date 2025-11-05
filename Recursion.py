#factorial(7)=7*6*5*4*3*2*1
def factorial(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n* factorial(n-1)
print(factorial(4))
#Question:Write a recursive function to print numbers from 1 to n.
def recursive(n):
    if (n==0):
        return 0
    else:
        recursive(n-1)
        print(n)
recursive(10)
#Question:Write a recursive function to find the sum of first n numbers.
def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
print(sum(10))
#Question.Write a programe of Fibonacci series.
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(10):
    print(fibo(i))
#Question:Write a recursive function to find sum of digits of a number.
def sumd(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumd(n//10)
print(sumd(1234456))
#Question:Write a recursive function to reverse a string.
def reverse(name):
    if len(name)==0:
        return name
    else:
        return reverse(name[1:])+name[0]
print(reverse("Manthan"))
