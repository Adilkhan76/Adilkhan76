'''d=(lambda a,b:a+b)(9,8)
print(d)
f=lambda a,b:a*b
print(f(1,2))'''

'''1. Write a python program to create a function that takes a list and returns
a new list with the original list's unique elements.'''

def takes_list(l):
    return [l[i]*2 for i in range(len(l))]
s=takes_list([1,2,3,4,5,6,7,8])
print(s) 

'''2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not.'''

def prime(num):
    for i in range(2,num+1):
        if num%i==0:
            break
    if num==i:
        print("The Given Number is Prime")
    else:
        print("The Given Number is not Prime")
prime(int(input("Enter any Number")))

'''3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]'''

def even():
    Sample_list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(Sample_list)):
        if Sample_list[i]%2==0:
            print(Sample_list[i])
even()

'''4. Write a python program to create a function that checks whether a passed string is
palindrome or not.'''

def palindrome(string):
     print("The Given String is Palindrome :") if string==string[::-1] else print('The Given String is not palindrome :')
palindrome(input('enter a string to verify that a string is palindrome or not'))
       

#5. Write a python program to create a function to find the Min of three numbers.
def min_():
    l1=[]
    t1=(123,4532,245,121,473,3836)
    for i in t1:
        if len(str(i))==3:
            l1.append(int(i))
    print(min(l1))
min_()
        

'''6. Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30.'''

def square():
    l2=[print(i**2,end=' ') for i in range(1,30)]
square()

#7. Write a python program to access a function inside a function.
def f1():
    print("f1")
    def f2():
        print('f2')
   
'''8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.'''
def accept(string):
    upper=lower=0
    for i in string:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        else:
            pass
    print("Number of upper case letter is %d"%upper)
    print("Number of Lower case letter is %d"%lower)
accept(input('enter any set of character'))


#9. Write a python program to create a function to check whether a string is a pangram or not.
def pangram(string):
    cout=0
    for s in range(len(string)):
        if string[s].isupper() or string[s].islower() or string[s]==' ':
            cout+=1
        else:
            print('The String is not Pangram')
            break
    if cout==len(string):
        print('The String is Pangram')
pangram(input('enter any string'))

#10. Write a python program to create a function to check whether a string is an anagram or not

def verify_pangram(string):
    cout=0
    for s in range(len(string)):
        if string[s].isupper() or string[s].islower() or string[s]==' ':
            cout+=1
        else:
            print('The String is not Pangram')
            break
    if cout==len(string):
        print('The String is Pangram')
pangram(input('enter any string'))