#1. Write a recursive python function to print first N natural numbers.
def natural_num(num):
    if num>0:
        natural_num(num-1)
        print(num)
natural_num(10)

#2. Write a recursive python function to print first N natural numbers in reverse order
def natural_num(num):
    if num>0:
        print(num,end=' ')
        natural_num(num-1)
natural_num(10)

#3. Write a recursive python function to print first N odd natural numbers
def natural_num(num):
    if num>0:
        natural_num(num-1)
        print(2*num-1)
natural_num(10)

#4. Write a recursive python function to print first N odd natural numbers in reverse order
def natural_num(num):
    if num>0:
        print(2*num-1)
        natural_num(num-1)
natural_num(10)
#5. Write a recursive python function to print first N even natural numbers.
def natural_num(num):
    if num>0:
        natural_num(num-1)
        print(2*num)
natural_num(10)

#6. Write a recursive python function to print first N even natural numbers in reverse order.
def natural_num(num):
    if num>0:
        print(2*num)
        natural_num(num-1)
natural_num(10)
#7. Write a recursive python function to print squares of first N natural numbers
def natural_num(num):
    if num>0:
        natural_num(num-1)
        print(num**2)
natural_num(10)
#8. Write a recursive python function to print cubes of first N natural numbers

def natural_num(num):
    if num>0:
        natural_num(num-1)
        print(num**3)
natural_num(10)
#9. Write a recursive python function to print first N multiples of a given number.
def natural_num(n,num):
    if num==1:
        return 1
    mul=n*natural_num(num-1)
    print(mul)
natural_num(5,10)
#10. Write a recursive python function to print a number in reverse order.
def natural_num(num):
    if num>0:
        print(num%10,end='')
        natural_num(num//10)
natural_num(int(input('enter any number to reverse')))