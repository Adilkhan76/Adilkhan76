#1. Write a python script to add comments and print “Learning Python” on screen.

print('''"Learning Python"''') # it(#) mark used to comment in python.

'''2. Write a python script to add multi line comments and print values of four variables,
each in a new line. Variable contains any values.'''

# To the multiline comment we have to write like as '''xzz'''
a,b,c,d=1,2,3,4            
print(a,b,c,d,sep='\n')

'''3. Write a python script to print types of variables. Create 5 variables each of them
containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)'''

i,j,k,l,m=35, True,'MySirG',5.46, 3+4j
print(type(i)),print(type(j)),print(type(k)),print(type(l)),print(type(m))

#4. Write a python script to print the id of two variables containing the same integer values.

x,y=1,1
print(id(x)),print(id(y))

'''5. Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable'''

r,s,t,u=12,12.33,True,'adil khan'
print("value=",r,",type=",type(r),",id=",id(r))
print("value=",s,",type=",type(s),",id=",id(s))
print("value=",t,",type=",type(t),",id=",id(t))
print("value=",u,",type=",type(u),",id=",id(u))

#6. Write a python script to print all the keywords
import keyword
print(keyword.kwlist)

#7. On Python shell use help() function and display the list of keywords

#we will write help() and then press enter button and after that we will write "keywords" 


'''8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py'''

# Description--> To this file you can consider it is as A0.py and we are importing A1.py file in A0.py.
import A1
print(A1.var1)

#9. Name the keywords, used as data in the Python script.

The answer is, True and False.

'''10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM)'''

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
print(dt_string)	