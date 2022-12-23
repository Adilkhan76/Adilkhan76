#1 Write a Python script to create a list of first N natural numbers.
[print(i+1,end=' ') for i in range(int(input('enter a number')))]
#2. Write a Python script to create a list of first N odd natural numbers.
l=[]
[l.append(2*i-1) for i in range(1,int(input('enter a number'))+1)]
print(l)
#3. Write a Python script to create a list of first N even natural numbers.
l=[]
[l.append(2*i) for i in range(1,int(input('enter a number'))+1)]
print(l)
#4. Write a Python script to find the greatest number in a given list of numbers.
l=[]
[l.append(int(input('enter a number'))) for i in range(int(input('enter limit')))]
print('Greatest Number is',max(l))
#5. Write a Python script to find the smallest number in a given list of numbers.
l=[]
[l.append(int(input('enter a number'))) for i in range(int(input('enter limit')))]
print('Lowest Number is',min(l))
#6. Write a Python script to calculate the sum of elements in a given list of numbers.
l=[]
[l.append(int(input('enter a number'))) for i in range(int(input('enter limit')))]
print('Total sum of list element is',sum(l))
#7. Write a Python script to remove all non int values from a list.
l=[10,12+3j,'adil',100.2,True,123,45]
for i in range(5):
    if type(int)!=type(l[i]):
        del(l[i])
print(l)

#8. Write a Python script to print distinct elements along with their frequencies of occurrence in list.
l=[]
[l.append(input('enter a number')) for i in range(int(input('enter limit to put element')))]
for i in range(len(l)):
    print(l[i],'-',l.count(l[i]))

#9. Write a Python script to print indices of all occurrences of a given element in a given list.
l=[]
[l.append(int(input('enter a number'))) for i in range(int(input('enter limit')))]
for i in range(len(l)):
    if l.count(l[i])>1:
        print(i,end=' ')
        for j in range(len(l)):
            if l[i]==l[j+i]:
                print(j)
            
    
#10. Write a python script to sort a list.
l=[]
[l.append(int(input('enter a number'))) for i in range(int(input('enter limit')))]
l.sort()
print(l)