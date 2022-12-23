#1. Write a python script to calculate sum of first N natural numbers

i=1
total=0
n=int(input('enter a number'))
while i<=n:
    total=total+i
    i+=1
print(total)

#2. Write a python script to calculate sum of squares of first N natural numbers
i=1
total=0
n=int(input('enter a number'))
while i<=n:
    total=total+(i**2)
    i+=1
print(total)

#3. Write a python script to calculate sum of cubes of first N natural numbers

i=1
total=0
n=int(input('enter a number'))
while i<=n:
    total=total+(i**3)
    i+=1
print(total)

#4. Write a python script to calculate sum of first N odd natural numbers

i=1
total=0
n=int(input('enter a number'))
while i<=n:
    total=total+(i*2-1)
    i+=1
print(total)

#5. Write a python script to calculate sum of first N even natural numbers

i=1
total=0
n=int(input('enter a number'))
while i<=n:
    total=total+(i*2)
    i+=1
print(total)

#6. Write a python script to calculate factorial of a given number
i=1
fact=1
n=int(input('enter a number'))
while i<=n:
    fact=fact*i
    i+=1
print(fact)
#7. Write a python script to count digits in a given number
i=0
n=int(input('enter a number'))
while n:
    n=n//10
    i+=1
print(i)

#8. Write a python script to calculate sum of digits of a given number
total=0
n=int(input('enter a number'))
while n:
    total=total+n%10
    n=n//10
print(total)

#9.Write python script to print binary equivalent of a given decimal number.(do not use bin() method)

print("Enter the Decimal Number: ")
dnum = int(input())
i = 0
bnum = []
while dnum!=0:
    rem = dnum%2
    bnum.insert(i, rem)
    i = i+1
    dnum = int(dnum/2)

i = i-1
print("\nEquivalent Binary Value is:")
while i>=0:
    print(end=str(bnum[i]))
    i = i-1
print()

#10. Write a python script to print the octal equivalent of a given decimal number.(do not use oct() method)
print("Enter the Decimal Number: ")
decnum = int(input())

i = 0
octnum = []
while decnum!=0:
    rem = decnum%8
    octnum.insert(i, rem)
    i = i+1
    decnum = int(decnum/8)

print("\nEquivalent Octal Value is: ")
i = i-1
while i>=0:
    print(octnum[i], end="")
    i = i-1
print()