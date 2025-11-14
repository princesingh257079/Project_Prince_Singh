#                             Day 1

print("Hello wolrd ")
if 5>2:
    print("5 is greater than 2")

x=5
y=3
print(x+y)
print(x*y)
print(x/y)
print(x-y)

print("this is python")

x=13
y="Prince"
print(x)
print(y)

x=4.5
print(type(x))

x=4
y=5
print(bool(x+y))
print(bool(x))


x=""
print(bool(x))
x="5"
print(bool(x))


my_var=40
print(my_var)


x,y,z="30", "40", "50"
x="30", "40" , "50"
print(x )

x=y=z="apple"
print(x)
print(y)
print(z)

fruits=["apple","banana0","cherry"]
x,y,z=fruits
x=y=z=fruits
print(x)
print(y)
print(z)
print(fruits)
print(type(x))
number=[2,4,7,8,34,50]
print(number)
print(type(number))

x="python"
y="is"
z="good"
print(x,y,z)
print(x+y+z)

#x=good

def my_func():
    print("python is "+ x)
    my_func()  

my_list=["apple", "banana", 1, 3, 5, 7]

my_list[2:5]=["abc"]

print(my_list)


text="hello"

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("hello", "world"))
print(text.split())

#format string

x="abc"
y=15
print(f"my name is {x} and my age is {y}") 

#                      DATA TYPE

x=5
print(type(x))

x=5.6
print(type(x))

x="Prince"
print(type(x))

x={"Apple","Banana"}
print(type(x))


#                       OPERATORS

# Arithmetic Operators in Python
a = 10
b = 3   


# Addition
add = a + b
print("Addition:", add)


# Subtraction
sub = a - b
print("Subtraction:", sub)


# Multiplication
mul = a * b
print("Multiplication:", mul)


# Division
div = a / b
print("Division:", div)


# Floor Division
floor_div = a // b
print("Floor Division:", floor_div)


# Modulus
mod = a % b
print("Modulus:", mod)


# Exponentiation
exp = a ** b
print("Exponentiation:", exp)


#assigment operators
x = 5
print("value of x:", x)


# Using += operator
x += 3             # x = x + 3
print("After using += operator, x:", x) 


# Using -= operator
x -= 2  # equivalent to x = x - 2
print("After using -= operator, x:", x) 


# Using *= operator
x *= 4                #  x = x * 4   
print("After using *= operator, x:", x)     


# Using /= operator
x /= 2                   #  x = x / 2
print("After using /= operator, x:", x)


# Using //= operator
x //= 2                  # x = x // 2
print("After using //= operator, x:", x)


# Using %= operator
x %= 3                    # x = x % 3
print("After using %= operator, x:", x)



#comparsion operators

x=5
y=10
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)
print(x<y) 


#logical operators

x=10
print(x>3 and x<11)
print(not(x>3))

#ldentity operators

x=[1,2,3]

y=x
z=[1,2,3]
print(x is y)



#                                     List

my_list=["Apple","Banana"]
print(type(my_list))
print(my_list)
print(len(my_list))

my_list=["Apple","Banana","Cherry"]
print(my_list[1])
print(my_list[-1])


my_list=["Apple","Banana","Cherry","Mango","Lemon","Coconut"]
# print(my_list[2:5])
print(my_list[-5:-2])



my_list=["Apple","Banana","Cherry","Mango","Lemon","Coconut"]
my_list[1]="Tomato"
print(my_list) 

 
#                                         # DAY-> 02
#                                       # 11/ 11 /2025
print("hello")

print("good morning")

my_list=["apple","banana",1,3,5,7]

my_list[2]="abc"

print(my_list)

y_list=["apple","banana",1,3,5,7]

my_list[2:5]=["abc"]

print(my_list)



my_list=[1,2,4,5,6]
my_list.insert(2,3)
my_list.append(7)

print(my_list)

list1=[1,2,3]
list2=[4,5,6]

list1.extend(list2)

print(list1)


#remove

list1=[1,2,3,"apple",4,5,6]


list1.remove("apple")
list1.pop()
print(list1)


list1=[]

list1.append(1)
print(list1)

list1[0]="hello"
print(list1)

#loopslists

list1=[1,2,3,4,4,4,"apple",5,6]
for x in list1:
    print(x)




#                              #Tuples
#     #A tuple is an ordered collection of items, similar to a list, but immutable (cannot change elements).
#     # tuples are defined using parenthese

#                                               #Python Set's
#                           #A set is an unordered collection of unique items.
# # . Sets do not allow duplicates.
# # . Sets are defined using curly braces{}.

 #Creating a Set      
colors={"red","green","blue"}
print(colors) 

 #Adding Elements
colors.add("yellow")
print(colors)

 #Removing Elements
colors.remove("green")
print(colors) 

 #Iterating Through Set
for color in colors:
    print(color)
                     

#                      #Python Dictionaries
# # A dictionary is an unorderedn collection of key-value pairs.
# # . Keys must be unique and immutable (string,number,tuple).
# # . Values can be any data type.
# # . Dictionaries are defined using curly braces {} with key: value.
                     
# Creating a DECTIONARY
student={"name":"Alice","age":45,"grade":"A+"}
print(student)

# ACCESSING VALUES 
print(student["name"]) # Alice
print(student.get("age")) # 20

# ADDING/UPDATING VALUES
student["age"]=21
student["city"]="Delhi"
print(student)

# REMOVING ITEMS
student.pop("grade")
del student["city"]
print(student)

# ITERATING THROUGH DICTIONARY
for key,value in student.items():
    print(key,":",value)



#                                   # IF....ELSE IN PYTHON
# # In Python, decision making is done using conditional statements. Sometimes, we want the program to make a choice depending on a condition.
# # For example:
# # . If you are above 18,you can vote.
# # . If you arebelow 18,you cannot vote.
# # This is possible using if,elif,and else statements.

# # 1. The if Statement
# # The if statement is used to check to check a condition.If the condition is true,the code inside will run.

# if else

age=20

if age>=18:
    print("you are adult")
else:
    print("you are not adult")   

#                                             # DAY-> 03
#                                             # 12/ 11 /2025  



#if else
  
age=16

if age<=18:
    print("you are adult")

elif age==18:
    print("you are teen")

elif age==17:
    print("you are 17")

else:
    print("you are not adult")  

    # 2 The if...else Statement.



    # 3. The if...elif...else Statement
    #    We can check multiple conditions using elif (else if).

a = 85

if a>=90:
    print("Grade:A+")
elif a>=80:
    print("Grade A+")  
elif a:
    print("Grade C")
else:
    print("Grade c")

#                        # 6. Nested If
#                  # WE CAN PUT AN IF INSIDE ANOYHER IF.      

x=15

if x>10:
    print("x is greater then 10")

if x>20:
    print("x is greater then 20")

else:
    print("x is not greater then 20")


#   # QUESTION-01 Write  program to check if a number is positive or negative.

x = 10

if x % 2 == 0:
    print("Even Number")
    
else:
    print("Odd Number")    


x=19

if x>=18:
    print("Good !! You are Eligible To Driving ")

else:
    print("Sorry !! You are Eligible To Driving")    


#                       # PYTHON FOR LOOPS 
# # A for loop in python is used to iterate (repeat) over a sequence such as a list,string,tuple, or range.

# # SYNTAX:

# # for variable in sequence:

# #code to execute
# # . variable -> takes the value of each item in the sequence one by one.
# # . The loop continues until all items are proceed.


word="python"
for x in word:
    print(x)

# # Using range()in For Loops
# # The range()function generates a sequenceof numbers.

for i in range(5):
    print(i)

#  # . You can also use range(start,stop,step)

for i in range(1,10,2):
    print(i) 

# #  4: Nested For Loops
# #  You can put a for loop inside another for loop.

for i in range(1,4):
    for j in range(1,3): 
       print(f"i={i},j={j}")


#  # 5: Using break in For Loops
#  # break stops the loop wwwwhen a conditin is met.

for i in range(1,6):
  if i==4:
    break
  print(i) 

#  # 6: Using continue in Foor Loops 

for i in range(1,6):
    if i==3:
        continue
    print(i)

#  #QUESTION NUM-> 1

for i in range(1,20):
    print(i)


#  #QUESTION NUM-> 2

for i in range(1,31):
    if i % 2==0:
        print(i) 

#  #QUESTION NUM-> 3





#  #QUESTION NUM-> 4

for i in range(1,4):
    for j in range(1,5):
        for k in range(1,6):
            print(f"i={i},j={j},k={k}")  
            

#                                      # PYTHON FUNCTION     
#  # 1. DEFINING A FUNCTION 
#  # Use the def keyword to define a function.

def greet():
     print("Hello,Python!")
greet() #calling the function 


#  # 2. FUNCTION WITH PARAMETERS
#  # Parameters allow you to pass values into a function.

def greet(name):
    print(f"Hello,{name}!")
greet("Alice")
greet("Bob")

#  # 3. FUNCTION WITH RETURN VALUE
#  # A function can return a value using the return statement.

def add(a, b):
    return a + b
result =add(5,3)
print(result) # 8

def add(a, b):
    return a - b
result =add(5,3)
print(result) # 8

def add(a, b):
    return a * b
result =add(5,3)
print(result) # 8

def add(a, b):
    return a / b
result =add(5,3)
print(result) # 8

#  # 4. FUNCTION WITH DEFAULT PARAMETER
#  # You can give a default value to a parameter.

def greet(name="Student"):
    print(f"Hello,{name}!")
greet() # Hello,Student! 
greet("Alice") # Hello,Alice!

# Scope of variables

x=10
def my_func():
    y=5
    print("Inside",x,y)
my_func()
print("Outside",x)

 # QUESTION NUM-> 01.

def greet(name):
    print(f"Hello,{name}")
greet("Prince")    

 # QUESTION NUM-> 02.

def add(a,b):
    return a + b
result =add(5,4)
print(result)

#                                         # OOPs IN PYTHON(BASIC)
# OOPs = Object-Oriented Programming System--->Organizing code using classes and objects.

# 1. CLASS AND OBJECT

# Class
class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Attribute
        self.color = color  # Attribute

    def drive(self):  # Method
        print(f"{self.color} {self.brand} is driving 🚗")

# Object
car1 = Car("BMW", "Black")
car2 = Car("Tesla", "White")

car1.drive()
car2.drive()


#                                         DAY -> 04
#                                        13/ 11 /2025

print("Hello Prince")
print("Good Morning")

#                                   PYTHON ARRAY'S 

# In Python, an array is a collection of items of the same type.

# . Unlike lists, arrays store elements of the same data type,Which makes them more efficient for large data
# . Python doesn't have a built-in array type like other languages, but we can use the array module or NumPy arrays.

# 1. Using Array Module
 
import array
number = array.array('i',[1,2,3,4,5])
print(number)

# 2. Accessing array Elements

import array
number = array.array('i',[1,2,3,4,5])
print(number[0]) 
print(number[3])

#                         RANDOM NUMBERS IN NUMPY

# NumPy  offers the random module to work with random numbers.

#            GENERATE RANDOM NUMBER

from numpy import random
x=random.randint(100)
print(x)

#            GENERATE RANDOM FLOAT

x=random.rand()
print(x)

#             GENERATE RANDOM ARRAY
from numpy import random

#              1 D Array

x=random.randint(100,size=(5))
print(x)

#            2 D Array

x=random.randint(100,size=(3,5))
print(x)

#            3 D Array

x=random.randint(100,size=(2,3,5))
print(x)

#            4 D Array

x=random.randint(100,size=(2,2,3,5))
print(x)


 # Generate Random Number From Array

from numpy import random
x = random.choice([4,5,6] , size=(5))
print(x)  

x = random.choice([4,5,6] , size=(2,3,5))
print(x)  

#                                  # PANDA'S IN PYTHON

#What is Pandas ? :  
#Pandas is a python library designed for data manipulation and analysis.
#The name "Pandas" comes from panel Data, which refers to multi-dimensional structured datasets.
#It is built on top of NumPy, so it supports fast mathematical operations.
#Pandas is widely used in Data Science,Machine learning , Finance, statics, and Research.


# Key Data Structure in Pandas 

# 1. Series
import pandas as pd
data = [10,20,30,40]
s=pd.Series(data) 

print(s)

#Creating a DataFrame 
# Similar to an Excel spreadsheet or SQL Table.
#A two dimensional data structure (rows X column)
data ={
    "Name": ["Alice","Bob","Charlie","David"],
    "Age": [24,27,22,32],
    "City" : ["Delhi","Mumbai","Chennai","Kolkata"]

}
df = pd.DataFrame(data)

print(df)

#b ) From a NumPy Array
import numpy as np

arr = np.array([1,2,3,4,5])
s=pd.Series(arr)
print(s)

#From a Dictionary

data ={"Maths":90, "Science":85,"English":78}
s=pd.Series(data)
print(s)

import pandas as pd
df = pd.read_csv("crocodile_dataset.csv")
print(df.head())
print(df.tail())






