# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:45:47 2020

@author: many and various

This is an example of using quotes to create a string which can be 
used to make comments.  This is actually three strings, two empty ones
and this one in the middle between the two empty strings.  Unlike
using hash marks, these strings are evaluated by the Python 
interpreter.  Because they are not assigned to a variable the have 
no real impact, but the practice does consume some resources.   

"""
#%%     Variables

x = 12 #initialize a variable called x 
print(x)

y = 13 #initialize a variable called y
print(y)

print ("the sum of",x,"and",y,"is", x+y)
#%%Different types of variables allowed in Python
# Integer vaiables can take only round numbers, both positive and negative

age = 12 # an integer variable
print(age)

#%% Numeric variables can take all real numbers. Also known as floating variables

pi = 3.14159
print(pi)
#%% Complex numbers have a real part and imaginary part
# the following represents 5 + 3j

complexExample = complex(5,3)

print("the real part of the Example is",complexExample.real)
print("the imaginary part of the Example is",complexExample.imag)
print(complexExample)

# Complex numbers can also be specified as follows
complexExample = 4+5j #Now our example has a real part of 4, imag = 5

# Since j = the square root of -1, we can take the square of
# the example and print it 

compSquared = complexExample**2
print(complexExample, " squared is ",compSquared)

#%% string variables can input test, string values must be betwen either
# single or double quotes.  if you need to have a quotation mark in the string
# use the escape charater '\'

text = "O'Brien said \"Beam me up Scotty!\""
print(text)

g = "half dozen"
h = 6   #We will use the str() function to convert the int to string
        #on the next line        
text = str(h) + " of one " + g + " of another"
print(text)

#%% Boolean variables, They take a binary value of either
# True or False.  Python is case sensitive.  True and False
# are special keywords reserved for Boolean values

boolExample = True
print("Is this a boolean value being printed?",boolExample)

#%% The following code lets you input values for first_name and
# last_name then combnes the two for output

first_name = input("First Name: ")
last_name = input("Last Name: ")

name = first_name + " " + last_name

print("Name =", name) 
#%% Math operator examples

x = 9
y = 4

z = x + y
print("The sum of",x,"and",y,"=",z)

z = x - y 
print("The difference of",y,"from",x,"=",z)

z = x * y 
print("The product of",x,"times",y,"=",z)

z = x/y 
print("The result of dividing",x,"by",y,"=",z)

z = x//y 
print("The quotient of",x,"divided by",y,"=",z)

z = x % y
print("The remainder of",x,"divided by",y,"=",z)

z = x**y
print(x,"raised to the power of",y,"=",z)

#%% The following are examples of comparison operators
# Comparison operators compares values on both sides of
# of the operator and respond with True or False value
# if the formulae is True or False.  These are used extensively
# for making decisions in workflows checks 
z = x>y
print("The statement",x,"is greater than",y,"is",z)

z = x<y
print("The statement",x,"is less than",y,"is",z)

if x == 9:
    print(x,"equals 9")
    
if x != 13:
    print(x,"is not equal to 13")

if x >= 6:
    print(x,"is greater than 6")

if x <= 20:
    print(x,"is less than 20")

#%% Logical operators -- There are 3 logical operators in Python
# and returns True if both values are True, otherwise it returns False
# or  returns True if either values is True, otherwise it returns False
# not returns the opposite value of the passed value.

a = True
b = False

print ("The and of a True and a False is",a and b)
print ("The or of a True and a False is",a or b)
print ("The not of a True is", not a)

#%% bitwise operators exist in Python as well.
# they operate on variables as if they were strings
# of binary digits.  This can be helpful for
# storing and manipulating data in condensed forms
# an example of this includes the Access Control Lists
# (ACLs) of Linux files rwx access = 7.
# bitwise operators are out of scope for this course.
# but here is one example:
    
x = 4 # bit pattern 0100
y = 9 # bit pattern 1001

z = 4 & 9 # returns a pattern where both inputs are 1
# in this case that is nowhere so z = 0

print("The bitwise AND of 4 & 9 is",z)

#%% Membership operators check is see if an item is present in another
# here are examples of them anyway. 'in' and 'not it'
# These functions are also used to step through a list if 
# values in for loops and other control functions
x = 'Hello world'
y = {1:'a',2:'b'}

testValue = 'H' in x
print("Is the letter 'H' in",x,"?",testValue)

# hello is not in 'Hello world' because case matters
testValue = 'hello' not in x
print("Is the word 'hello' not in",x,"?",testValue)

testValue = 1 in y
print("Is the value 1 present in",y,"?",testValue)

testValue = 'a' in y 
print("Is the value 'a' present in",y,"?",testValue)

# Examples of the use of in for For loops appears later
#%% Also outside the scope of the course are identity operators
# they are used to determine if two variables are pointing to the 
# exact same memory address or not:  'is' and 'is not'
# Their usage provides insight into how Python manages memory
# this gets complicated and so no examples are provided here.

#%% Assignment operators 
# Addition, subration and multiplication can be done within
# a line of code as in the following examples
# an <operation>= operator exists for all the math operators

x = 9
print("x before plus equals 4 is",x)
x += 4
print("x after plus equals 4 is",x)

x = 9
print("x before minus equals 4 is",x)
x -= 4
print("x after minus equals 4 is",x)

x = 9
print("x before times equals 4 is",x)
x *= 4
print("x after times equals 4 is",x)

x = 9
print("x before divide equals 4 is",x)
x /= 4
print("x after divide equals 4 is",x)

x = 9
print("x before quotient equals 4 is",x)
x //= 4
print("x after quotient equals 4 is",x)

x = 9
print("x before remainder equals 4 is",x)
x %= 4
print("x after remainder equals 4 is",x)

# There exist assignment operators for most of the bitwise 
# operators as well. Left as an exercise for the student to investigate

#%% Python has some non-primitive data types:
# Lists, Tuples, Arrays and Dictionaries.

# Lists can take multiple values of different data types.
# You can think of them as a row from a table, or records
# in a data set.
# Lists can be initialized by using an ordered set of values between square brackets "[]"

list1 = [2,3,5,7,11,13,17,19,23] # the first 9 prime numbers
print("The first nine prime numbers are",list1)

list2 = ["Mercury","Venus","Earth","Mars"] # The 4 rocky planets in the Sol system
print("The local rocky planets are",list2)

list3 = ["Lift off","in",5,4,3,2,1,"lift off"] #numbers and strings in a list
print("A mixed list",list3)

# extracting data from a list or indexing can be done by specifying 
# an address in the list.  Lists can also be changed in this way
# the first position in a list is 0, the last is -1 the second to last is -2

print ("The second value in the list is",list3[1])
print ("The last value in the list is ", list3[-1])

# multile values in a list can be accessed by using a list of the locations
# you want to extract.  But items can only be extracted one at a time.

b = [1,3,5]
c = [list3[i] for i in b]
print("\nThe second, fourth and sixth values of \n",list3,"\n are",c) 
# returns the second, fourth and sixth values in the original list
# the \n inserts a newline character
 
d = [list3[0],list3[2],list3[4]]
print("\nThe first, third and fifth values of \n",list3,"\n are",d) 

# Values can also be retrieved using a vector
# 1:3 creates an array [1,2] as the values start at the first value
# and ends before the last value (different syntax than [R] for example)

print("\nThe second and third values of \n",list3,"\n are",list3[1:3]) 

#%% tuples
# A tuple is a collection of Python objects separated by 
# commas. In someways a tuple is similar to a list in terms 
# of indexing, nested objects and repetition but a tuple is 
# immutable unlike lists which are mutable.  Immutables means
# that once a tuple is created individual elements in the tuple
# cannot be changed.  New values can be assigned to the variable
# as a whole.
# Tuples are also different from lists in that when they are 
# created use either nothing or parenthesis "()" to contain
# the elements in the tuple

tupleExample1 = 1, "Dog", "Happy", 3.14159
tupleExample2 = (1, "Dog", "Happy", 3.14159)

equalTest = tupleExample1 == tupleExample2
print ("Is",tupleExample1,"the same as",tupleExample2,"?",equalTest)

# elements in a tuple can be accessed using typical indexing
# The first element is element zero, the last is element -1

print("How do we feel?",tupleExample2[2]) #Third element
print("What are we? a",tupleExample2[-3]) #Third from the end

# but the cannot be changed, the following will generate an error
# This also is an example of error handling
# the try statement is matched by one or more 
# except statements.  If an error occurs control
# jumps to the except.  If no error occurs, the
# except code is bypassed.

print()
print("We will now try to change a value in a tuple")
try:
    tupleExample2[2] = "Sad"
except TypeError as err:
    print("Handling type-error:",err)
print()
# tuples (continued) because the last error keeps the code from 
# running. But you can reassign the entire variable

tupleExample2 = 12
print("We changed the tupleExample2 variable to",tupleExample2)

# tuples can also be multi-dimensional.  The following code
# creates a 2 x2 tuple, with a then slices and dices it
tp2 = (((1,2,3), (4,5,6)), ((7,8,9), (10,11,12)))
print("What does the new full tuple look like?")
print(tp2)
print("The first row is",tp2[0])
print("The second element in the first row is",tp2[0][1])
print("The second element in the second row is",tp2[1][1])
print("The first item, in the second element of the second row is",tp2[1][1][0])

#%% Arrays
# Arrays in Python are like lists but the type of variable
# held in the array is defined when the array is created and only
# that type of variable can be stored in the array thereafter. 
# You create an array using the array function.
# importing "array" for array creations 
# refer to https://docs.python.org/3/library/array.html for the types of arrays
import array as arr 
  
# array with int type 
a = arr.array('i', [1, 2, 3, 4]) 
  
print ("Array after initialization : ", end =" ") 
for i in range (0, 4): 
    print (a[i], end =" ") 
print() 
  
# inserting array using  
# insert() function 
a.insert(1, 4) # This inserts the value into the array before 
               # position 2
  
print ("Array after insertion : ", end =" ") 
for i in (a): 
    print (i, end =" ") 
print()  
  
# array with float type 
b = arr.array('d', [2.5, 3.2, 3.3]) 
  
print ("Array before append ", end =" ") 
for i in (range (0, 3)): 
    print (b[i], end =" ") 
print() 
  
# adding an element using append() 
b.append(4.4) 
  
print ("Array after append ", end =" ") 
for i in (b): 
    print (i, end =" ") 
print() 

# pop takes the last value out of the array 
testEx = b.pop()  
print("The value poped out of the array is",testEx)

print ("Array after pop ", end =" ") 
for i in (b): 
    print (i, end =" ") 
print() 

#%% Dictionaries allow the defining of a set of 
# Key Value pairs.  Dictionaries use curly brackets 
# when they are being defined "{}"
# After the dictionary is defined, values can 
# be looked up by using the key.
# the following code gives examples of some of the typical 
# dictionary manipulation commands for a full list and 
# additional examples try this site: https://www.w3schools.com/python/python_dictionaries.asp

band ={"james":"guitar", "kirk":"guitar", "jason":"base", "sarah":"voice","Lars":"drums"}
print(band)

# The keys for this dictionary can be retrieved using the keys() method

keys = list(band.keys())
print(keys)

values = list(band.values())
print(values)

# the membership functions can be used to check for the 
# for keys or values in a dictionary
check = "dave" in band # by default in looks in the keys
print("Is dave in the band:", check)

check = "guitar" in band.values()
print("Does someone play a guitar in the band:",check)

# here are two diffeent syntaxes for getting values
# out of a dictionary using the key
print("What instrument does james play?",band.get("james"))
print("What instrument does jason play?",band["jason"])

# you can remove a value from the dictionary using the pop method
print("The dictionary looks like this before poping jason")
print(band)
print("It is ",len(band),"elements long")
print()

band.pop("jason")

print("Now it looks like this")
print(band)
print("It is ",len(band),"elements long")
print()

#To add jason back
band["jason"]="bass"
print("With jason added back in, the dictionary now looks like:")
print(band)

# all key value pairs in the dictionary can be removed with the clear method

band.clear()
print("The empty band looks like this:",band)

#to delete the dictionary completely
del band

#%% Conditional statements
# if else statements require careful indentation
# Spyder helps you with this.

x=12
y=13

# The following is a simple if else statement
# allow you to test a condition and then do one
# thing if the test is True and another if False
if x>y:
    print(x,"Is greater than",y)
else:
    print(x,"is not greater than",y)

# But the if else can have many layers allowing 
# many tests by using the elif statement
if x>y:
    print(x,"Is greater than",y)
elif x==y:
    print(x,"is equal to",y)
else:
    print(x,"is less than",y)
    
#%% Loops
# First the for loop 
# The for loop iterates over a list of values and
# executes the code in the loop for each value 
# in the list (Unless the for loop is exited)
# Please note the colon in the syntax

runningList = [1,2,3,4,5,6,7,8,9,10] # initialize a list

for i in runningList: # i is the variable we define which will iterate through the list
               # taking each value in turn until the contents of the list is exhausted 
    print(i,"times 19 =",i*19) # The print will display the times values for 19

# another way to drive a for list is with the range command

for i in range(10): # range(10) creates a list with 10 values 
    print(i)        # starting at 0 and ending at 9
    
for i in range(12,23): # when range is given a start and end value 
    print(i)           # it will start at the low value and then increment
                       # up to but not including the high value
for i in range(20,10,-2): # the range can be defined in decreasing order
    print(i)              # with different step values
    
# The list to iterate over does not need to be numeric

student = ["mark","rob","tom","kevin"]    

for name in student:
    print("Student name is",name)
    
# If the list being iterated over is empty the 
# for loop is not executed

for i in range(10,20,-1):
    print("We never get here!!!")

#%% The while loop 
# while loops test a condition.  If the test returns a True then the 
# code in the while loop gets executed, otherwise the program exits the loop

count = 10 

while (count > 0): 
    print("the count is now:",count)
    count -= 1
     
print("The last value of count is",count)

while (count > 10):  #If the condition is never true, the body of the code is not executed
    print("We don't get here!")
    

#%% The break statement: break statements are used to stop the execution
# of the for loop code. When a break command is executed, control moves to
# the part of the code directly after the for loop

print("We will stop when we hit the y in apocalypse")

for letter in "apocalypse":
    if letter == "y":
        break
    else:
        print (letter,end="") # end ="" leaves the cursor write after the output
                              # the default is to add a newline

print() # to get the newline
    
# The continue statement; continue statements halt the execution of this
# iteration and move control back to the for statement which executes the 
# next iteration if there is one.

print("We will skip over the letter y in apocalypse")

for letter in "apocalypse":
    if letter == "y":
        continue
    else:
        print (letter,end="")
   
print() # to get the newline

#%% functions
# functions are useful when you want to define a task that will be 
# performed many times. Functions are defined by using the keyword def
# followed by the name of your function with the number of input fields in 
# paranthesis "()" a colon ":" then the code to execute

def hypotenuse(x,y): # we are defining a function to calculate the length
                     # of a hypotenuse of a triangle.    
    import math      # the square root function is part of the math library
                     # so we import that to make it available.
    h = (x**2) + (y**2)
    h = math.sqrt(h)
    return h

hyp = hypotenuse(3,4)
print("the hypotenuse of a triangle with sides of length 3 and 4 is",hyp)

hyp = hypotenuse(5,12) # The function can be called as often as needed
print("the hypotenuse of a triangle with sides of length 5 and 12 is",hyp)

def testFact(x):  # functions can be recursive (call themselves)
    print("In testFact with x =",x)
    if x == 1:
        return 1
    else:
        return x * testFact(x-1)

print("Calling testFact with an input of 4")
y = testFact(4)
print("4 Factorial = ",y)
