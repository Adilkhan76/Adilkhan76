1. Write a python script to reverse a number.
number=int(input('enter a number'))
while number:
    print(number%10,end='')
    number=number//10
    
#2. Write a python script to check whether a given number is Prime or not
number=int(input('enter a number'))
i=2
while i<=number:
    if number%i==0:
        break
    if i==number:
        break
    i+=1
if number==i:
    print('prime number')
else:
    print('not')
    
    
#3. Write a python script to print all Prime numbers under 100
i,j,k=2,2,0
while k<=100:
    while j<=i:
        if i%j==0:
            break
        j+=1
    if j==i:
        print(i,end=' ')
        k+=1
    i+=1
    j=2
#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
n=int(input('enter a number'))
m=int(input('enter a number'))
i=2
while n<m:
    while i<=n:
        if n%i==0:
            break
        i+=1
    if n==i:
        print(i,end=' ')
    n+=1
    i=2

#5. Write a python script to find next prime number of a given number
n=int(input('enter a number'))
n+=1
i=2
while 1:
    while i<=n:
        if n%i==0:
            break
        i+=1
    if n==i:
        print(i,end=' ')
        break
    n+=1
    i=2

#6. Write a python script to print first N prime numbers
n=int(input('enter a number'))
i,j,k=2,2,0
while k<=n:
    while j<=i:
        if i%j==0:
            break
        j+=1
    if j==i:
        print(i,end=' ')
        k+=1
    i+=1
    j=2
#7. Write a python script to print first N terms of a Fibonacci series
n=int(input('enter a number'))
i,a,b=1,-1,1
while i<=n:
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    i+=1

#8. Write a python script to calculate LCM of two numbers
x=int(input('enter first number'))
y=int(input('enter second number'))
if x > y:
       greater = x
else:
    greater = y

while(True):
    if((greater % x == 0) and (greater % y == 0)):
        lcm = greater
        break
    greater += 1
print("The L.C.M. is",lcm)

#9. Write a python script to calculate HCF of two numbers
num1=int(input('enter first number'))
num2=int(input('enter second number'))

hcf = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("Hcf of", num1, "and", num2, "is", hcf)