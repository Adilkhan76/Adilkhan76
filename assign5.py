'''1. Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)'''

print(int(input('enter a number'))//10)

'''2. Write a python script to get the last digit from a given number. (for example, if user
enters 2089 then your output should be 9)'''

print(int(input('enter a number'))%10)

#3. Write a python script to swap data of two variables

a,b=1,2
b,a=a,b
print(a,b)

#4. Write a python script to find x power y, where values of x and y are given by user
 
print(int(input('enter a number'))**int(input('enter a power')))

#5. Write a python script which takes a three digit number from the user and displays only its first digit.
print(int(input('enter 3 digit number'))//100)


'''6. Write a python script which takes a three digit number from the user and displays
only its middle digit.'''

print((int(input('enter 3 digit number'))//10)%10)

'''7. Write a python script which takes a three digit number from the user and displays
only its last digit.'''

print(int(input('enter 3 digit nmber'))%10)

#8. Write a python script to use IN operator to display the data present in the list
l1=[12,34,56,67,23]
n=int(input('enter number'))
if n in l1:
    print(n)

#9. Write a python script to use NOT IN operator to display the data not present in list
l1=[12,34,56,67,23]
n=int(input('enter number'))
if n not in l1:
    print(n)


