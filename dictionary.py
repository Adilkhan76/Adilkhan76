#1. Write a python program to create and print a dictionary which stores your information. (name, age, gender .....)

d1={'name':'adil','age':21,'gender':'male','address':'pilibhit'}
print(d1)

2. Write a python program to access the items of a dictionary by referring to its key name.

d2={1:1,2:4,3:9,4:16,5:25,6:36,7:49}
print(d2[2],d2[7],end=' ')

#3. Write a python program to get a list of the values from a dictionary.

squares={x:x*x for x in range(7)}
l1=[]
for i in range(len(squares)):
    l1.append(squares[i])
print(l1)

#4. Write a python program to change the value of a specific item by referring to its key name.

d2={1:1,2:4,3:9,4:16,5:25,6:36,7:49}
d2[7]=50
print(d2)

#5. Write a python program to print all key names in the dictionary, one by one.
d3={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f'}
print(d3.keys())
print(d3.values())

#6. Write a python program to create a dictionary that contains three dictionaries. (nested)

d={0:{1,2,3},1:{'adil','khan'},2:{7,8,9}}
print(d)
for i in range(len(d)):
    print(d[i],end=' ')

'''7. Write a python program to create three dictionaries, then create one
dictionary that will contain the other three dictionaries'''

d1={1:'adil',2:'khan'}
d2={3:'tahir',4:'khan'}
d3={5:'fazil',6:'khan'}
d4={}
d4.update(d1),d4.update(d2),d4.update(d3)
print(d4)

'''8. Write a python program to convert two lists into a dictionary in a way
that item from list1 is the key and item from list2 is the value'''

l1=[x for x in range(5)]
l2=[x*x for x in range(5)]
d1={}
for i in range(len(l1)):
    d1.update({l1[i]:l2[i]})
print(d1)

#9. Write a python program to merge two python dictionaries into one dictionary.
d1={1:'a',2:'b'}
d2={3:'c',4:'d'}
d3={**d1,**d2}
print(d3)

'''10 Write a python program to get the key of lowest value from the dictionary.
sample_dict = {'C': 92,'Java': 66,'Python': 85}'''

s=min(sample_dict.values())
e={key for key in sample_dict if sample_dict[key]==s}
print(e)
