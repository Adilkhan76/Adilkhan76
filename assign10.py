#1. Write a python script to print the first 10 multiples of 5.
i=1
while i<=10:
    print(i*5,end=' ')
    i+=1
#2. Write a python script to print first 10 multiples of N
i=1
n=int(input('enter a number'))
while i<=10:
    print(i*n,end=' ')
    i+=1
#3. Write a python script to print first M multiples of N.
number=int(input('enter a number'))
upto=int(input('enter a number'))
i=1
while i<=upto:
    print(i*number)
    i+=1
#4. Write a python script to print the first 10 multiples of N in reverse order.

i=10
n=int(input('enter a number'))
while i>=1:
    print(i*n,end=' ')
    i-=1
#5. Write a python script to print table of user’s choice
i=1
n=int(input('which one table you want to print'))
while i<=10:
    print(i*n,end=' ')
    i+=1
#6. Write a python script to print first N even natural numbers.

i=1
n=int(input('enter a number'))
while i<=n:
    print(2*i,end=' ')
    i+=1
#7. Write a python script to print first N odd natural numbers

i=1
n=int(input('enter a number'))
while i<=n:
    print(2*i-1,end=' ')
    i+=1
#8. Write a python script to print squares of first N natural numbers.
i=1
n=int(input('enter a number'))
while i<=n:
    print(i**2,end=' ')
    i+=1
#9. Write a python script to print cubes of first N natural numbers.
i=1
n=int(input('enter a number'))
while i<=n:
    print(i**3,end=' ')
    i+=1
#10. Write a python script to display all prime numbers within a range.
# range start = 15 and end = 45.

start,end=15,45
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
    