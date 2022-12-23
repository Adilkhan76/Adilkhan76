#1. Write a python script to create a String in 3 different possible ways
string='adil khan'
name=input('enter anything')
print(string,name,sep='\n')
#2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
string='iNeuron'
print(string[5::2])
#3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)
string='Hello Learners'
print(string[2:6:1])
#4. Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )
a,b='Learning','Python'
print(' '.join([a,b]))

#5. Write a python script to get the count of total number of characters in String a= “iNeuron”
string="iNeuron"
print("Tota Number of character in a string is" ,len(string))
#6. Write a python script to reverse a String. (“iNeuron”)
string='iNeuron'
print(string[::-1])
#7. Write a python script to determine whether a string contains a specific substring.
string=input('enter a string')
substring=input('enter a substring')
print(substring in string)
#8. Write a python script to check if a string contains only numbers.
string=input('enter string')
print("Yes the string contains only numbers",string.isnumeric())

#9. Write a python script to check if a string contains only characters of the alphabet.
string=input('enter a string')
print(string.isalpha())

#10. Write a python script to convert an integer to a string.
integer=int(input('enter any number'))
print(type(str(integer)))