#1. Write a python program to create a simple function which prints “MySirG”
def Print():
    print('''"MySirG"''')
Print()

#2. Write a python program to create a function which expects two arguments and print them in the function body.
def Takes_Two(a,b):
    print(a,b,end=' ')

#3. Write a python program to create a function which expects an unknown number of arguments.
def my(*args):
    print(type(*args))
    for num in args:
        print(num,end=' ')
my(1,2,3,4,5,56)



#4. Write a python program to create a function which expects kwargs arguments.
def greet(name,msg="How are you ?"):
    print(name,msg,end=' ')
greet('Adil Khan,')

#5. Write a python program to create a function which expects a list as an argument.
def f1_list(x):
    print(x)
f1_list([1,2,3,4,5,6,7,8,9])
    
#7. Write a python program to sum all the numbers in a list.
def f1_list(x):
    print(sum(x))
f1_list([1,2,3,4,5,6,7,8,9])

#8. Write a python program to multiply all the numbers in a list.
def f1_list(x):
    mul=1
    for i in range(len(x)):
        mul=mul*x[i]
    print(mul)
f1_list([1,2,3,4,5])

#9.Write a python program to create a function to check whether a number falls in a given range.
def f1(a):
    num=int(input("enter a number"))
    for i in a:
        if num==i:
            print("The number is in the given range:")
            break
        else:
            pass
    else:
        print("The number is not in given range")
f1(range(1,int(input('enter a limt'))))

#10. Write a python program to create a function to check whether a given number is even or odd

def verify(num):
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
verify(int(input("enter a number")))