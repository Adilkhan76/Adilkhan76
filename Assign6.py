#1. Write a python script to check whether a given number is positive or non-positive

num=int(input('enter a number'))
if num>0:
    print('positive')
elif num==0:
    print('non positive')
else:
    pass

#2. Write a python script to check whether a given number is divisible by 5 or not

num=int(input('enter a number'))
if num%5==0:
    print('divisible')
else:
    print('not divisible')


#3. Write a python script to check whether a given number is even or odd
num=int(input('enter a number'))
if num%2==0:
    print('even')
else:
    print('odd')

'''4. Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same.'''

num1=int(input('enter a number'))
num2=int(input('enter a number'))
if num1==num2:
    print('Numbers are the same')
elif num1>num2:
    print('num1 is greater')
else:
    print('num2 is greater')

#5. Write a python script to print two given words in dictionary order

w1=input('enter first word')
w2=input('enter second word')
if w1>w2:
    print(w2)
    print(w1)
else:
    print(w1)
    print(w2)


#6. Write a python script to check whether a given number is a three digit number or not.

num=int(input('enter 3 digit number'))
i=0
while num>0:
    num=num//10
    i+=1
if i==3:
    print('this is 3 digit number')
else:
    print('not')

#7. Write a python script to check whether a given number is positive, negative or zero.

num=int(input('enter a number'))
if num>0:
    print('positive')
elif num<0:
    print('negative')
else:
    print('non-positive') 


#9. Write a python script to check whether a given year is a leap year or not.

year=int(input('enter year'))
if year%4 and year%100 or year%400==0:
    print('leap year')
else:
    print('not')

'''10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.'''

num1=int(input('enter a number'))
num2=int(input('enter a number'))
num3=int(input('enter a number'))
if num1>num2:
    print('num1 is greater',num1)
elif num1<num2:
    print('num2 is greater',num2)
else:
    print('num3 is greater',num3)


'''11. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part'''

comp=complex(input('enter a complex number'))
if comp.real>comp.imag:
    print('real number is greater')
else:
    print('imaginary number is greater')

