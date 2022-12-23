#1. Write a python program to store all the programming languages known to you using Set.
n=int(input('how many programming language do you want to enter'))
s=set()
for i in range(n):
    s.add(input('enter one language'))
print(s)

#2. Wap to store your own information {name, age, gender, so on..}

s1={'Name=Adil Khan','Age=17','Gender=Male','Adress=Uttar Pradesh'}
s1.add(input("enter your father name"))
print(s1)

#3. Write a python script to get the data type of a Set.
s2={12,12.3,'adil',3+4j,(1,2,3)}
print(type(s2))

#4. Write a Python script to find if “Python” is present in the set thisset = {"Java", "Python", "Django"}

thisset = {"Java", "Python", "Django"}
print('Python' in thisset)

#5. Write a python program to add items from another set to the current set.

thisset = {"Java", "Python", "SQL"}
secondset= {"C","java", "Cpp", "NoSQL"}
print(thisset.union(secondset))

#6. Write a python program to add elements of list to a set

thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset=thisset.union(mylist)
print(thisset)

#7. Write a python program to remove last item of the given set

thisset = {"Python", "Django", "JavaScript", "SQL"}
print(thisset.pop())

#8. Write a python program to delete the set completely.
this = {"Python", "Django", "JavaScript", "SQL"}
print(this)
del(this)
print(this)

#9. Write a python program to loop through the set and print values
thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset=list(thisset)
for i in range(len(thisset)):
    print(thisset[i],end=' ')

#10. Write a python program to find the maximum and minimum value in a set.
this={10,20,30,40,34,23,18}
print("maximum value is %d"%max(this))
print("minimum value is %d"%(min(this)))