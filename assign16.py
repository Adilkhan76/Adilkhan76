'''1. Write a python script to store multiple items in a single variable
( Items are “Java”,“Python”, “SQL”, “C” ) using tuple'''

Tuple=('java','python','SQL','C')
print(Tuple)

#2. Write a python program to store only one item using tuple.
t=('apple',)
print(t)

#3. Write a python program to reverse the tuple.
Tuple=('java','python','SQL','C')
print(Tuple[::-1])

#4. Write a python program to Swap two tuples in Python.
a=('This','is','first','tuple')
b=('This','is','second','tuple')
temp=()
temp=a
a=b
b=temp
print(a,b,sep='\n')

#5. Write a python program to check if all items in the tuple are the same.
data=(11,11,11,11)
if data.count(data[0])==len(data):
    print("same items in a tuple")
else:
    print('not same')

#6. Write a python program to divide the tuple into four variables.
tuple1=(100, 200, 300, 400)
a,b,c,d=tuple1[0],tuple1[1],tuple1[2],tuple1[3]
print(a,b,c,d,end=' ')

7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)

tuple2=(1,2,3,4,5,6)
tuple3=[]
for i in tuple2:
    if i>3 and i<6:
        tuple3.append(i)
print(tuple3)

#8. Write a python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))


tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
a=()
b=()
temp=()
for i in range(len(tuple1)):
    a=tuple1[i]
    b=tuple1[i+1]
    if a[1]>b[1]:
        temp=tuple1[i]
        tuple1[i]=tuple1[i+1]
        tuple1[i+1]=temp
print(tuple1)

#9. Write a python program to print the value 20 from given nested tuple tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
tuple1=('python',[10,20,30],(2,4,16))
temp=()
for i in range(len(tuple1)):
    temp=tuple1[i]
    for j in range(len(temp)):
        if temp[j]==20:
            print(temp[j],type(temp),end=' ')
#10. Write a python program to change the first item (22) of a list within the following tuple to 222.
#tuple1 = (11, [22, 33], 44, 55)
            
tuple2 = (11, [22, 33], 44, 55)
tuple2=list(tuple2)
temp=[]
for i in range(len(tuple2)):
    temp=tuple2[i]
    if type(temp)==list:
        for j in range(len(temp)):
            if temp[j]==22:
                temp[j]=222
                tuple2[i]=temp
tuple2=tuple(tuple2)
print(tuple2)
