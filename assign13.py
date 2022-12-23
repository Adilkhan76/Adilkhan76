'''1. Write a python script to store multiple items in a single variable
(Items are “Java”,“Python”, “SQL”, “C” ) using list'''

l1=[]
for i in range(int(input('how many items you want to store'))):
    l1.append((input('enter item')))
print(l1)



#2. Write a python script to get the data type of a list.

l=[1,2,3,4,5,6,7,8]
for i in l:
    print(i ,end=' ')

#3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])

mylist = ["Java", "C", "Python"]
print(mylist[-1])

'''4. Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"] '''

l=['java','SQL','C','Reactnative','Javascript','python']
print(l)
l[1]='NoSQL'
l[3]='Flutter'
print(l)

'''5. Write a python script to add an item to the end of the list (item “Python”. (mylist =
["Java", "SQL", "C", "Reactnative"]'''

mylist =["Java", "SQL", "C", "Reactnative"]
mylist.append('Python')
print(mylist)

'''6. Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )'''

firstlis = ["Java", "Python", "SQL"]
secondlis = ["C", "Cpp", "NoSQL"] 
print(firstlis+secondlis)



'''7. Write a python program to Print all items by referring to their index number (thislist =
 ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]'''

thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for i in range(6):
    print(thislist[i],end=' ')
    

'''8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
"C", "Reactjs", "Javascript", "Python"]'''

thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
print(sorted(thislist))

#9. Write a Python script to create a list of city names taken from the user.

n=int(input('enter a limit'))
l1=[]
for i in range(n):
    l1.append(input('enter city name'))
print(l1)

#10. Write a Python script to create a list, where each element of the list is a digit of a given num
list_1=[]
n=int(input('enter a number'))
while n:
    r=n%10
    list_1.append(r)
    n=n//10
print(list_1[::-1])
