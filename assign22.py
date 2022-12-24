#1. Write a recursive python function to calculate sum of first N natural numbers
def sumofnatural(num):
    if num==1:
        return 1
    return num+sumofnatural(num-1)
print(sumofnatural(int(input('enter a number'))))

#2. Write a recursive python function to calculate sum of first N odd natural numbers
def sumofnatural(num):
    if num==1:
        return 1
    
    return (2*num-1)+sumofnatural(num-1)
print(sumofnatural(int(input('enter a number'))))

#3. Write a recursive python function to calculate sum of first N even natural numbers
def sumofnatural(num):
    if num==1:
        return 2
    return (2*num)+sumofnatural(num-1)
print(sumofnatural(int(input('enter a number'))))

#4. Write a recursive python function to calculate sum of squares of first N natural numbers
def sumofnatural(num):
    if num==1:
        return 1
    return (num**2)+sumofnatural(num-1)
print(sumofnatural(int(input('enter a number'))))
#5. Write a recursive python function to calculate sum of cubes of first N natural numbers
def sumofnatural(num):
    if num==1:
        return 1
    return (num**3)+sumofnatural(num-1)
print(sumofnatural(int(input('enter a number'))))
#6. Write a recursive python function to calculate the factorial of a number.
def sumofnatural(num):
    if num==1:
        return 1
    return (num)*sumofnatural(num-1)
print(sumofnatural(int(input('enter a number'))))

#7. Write a recursive python function to calculate sum of the digits of a given number

def sumofnatural(num):
    if num==0:
        return 0
    return (num%10)+sumofnatural(num//10)
print(sumofnatural(int(input('enter a number'))))

#8. Write a recursive python function to find the Nth term of the Fibonacci series.
# nth term of Fibonacci series using recursion
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# Reading number of terms
term = int(input("Which term of Fibonacci series? "))
result = fib(term)
print(result)
