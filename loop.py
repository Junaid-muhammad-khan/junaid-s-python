names = ["ali" , "ahemd" , "junaid"]

for me in range(len(names)):
    names[me] = "Mr." + names[me]

print(names)


my_fruits = ["apple" , "banana" , "orange"]
for fruits in my_fruits:
    print("i love" , fruits)

names0 =  ["ali" , "ahemd" , "junaid" , "waris" , "ahsan" , "gorrila"]
names0.remove("gorrila")
for listofnames in names0: 
    print("Mr." , listofnames)

my_fruits0 = ["apple" , "banana" , "orange"]

for fruitss in range(len(my_fruits0)):
    my_fruits0[fruitss] = "i love " + my_fruits0[fruitss]

print(my_fruits0)

vegatable_basket = {"tomato" : 4 , "peas" : 2}
for vegetable, count in vegatable_basket.items():
    print("there are" ,count, vegetable, "in the vegetablebsket")

alphabets = ["a","b","c"]

for alphabetsind, alp in enumerate(alphabets):
    print("the number", alp,"is on" , alphabetsind, "index")

most_selling_cars = ["supra" , "bugatti" , "lamborgini"]

for index, car in enumerate(most_selling_cars):
    print("the" , car, "is on rank", index)

students_of_class =  ["ali" , "ahemd" , "junaid" , "waris" , "ahsan" , "gorrila"]

for ranks, students in enumerate(students_of_class):
    print(students,"got", ranks , "rank in the class")

# While Loop
# With the while loop we can execute a set of statements as long as a condition is true it wont stop until laptop blasts.
# So for that we need some special operators
i = 1
while i < 6:
    print(i)
    i += 1

# Break statement

i = 1
while i < 5:
    print(i)
    if i == 3: # Exit the loop when i is 3
        break
    i += 1

# Countinue statament

i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# For Loop

for x in "banana":
  print(x) 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:                        # Do not print banana
  if x == "banana":
    continue
  print(x)

# Range

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)

# Else 
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested Loop

adj = ["red", "big", "tasty"]
fruits90 = ["apple", "banana", "cherry"]
for x in adj:                           #The "inner loop" will be executed one time for each iteration of the "outer loop":
  for y in fruits90:
    print(x, y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass


for me in range(1,100,2):
   print(me)

count0 = 1

# This code mean: im junaid will print untill count is lessthen or equal to 10
while count0 <= 10:
  print(count0 ,"imjunaid")
  count0 += 1 # this mean count will increase by 1 always after it is running

h = 5
while h >= 1:
   print(h)
   h -= 1

# Infinite loop

"""
l = 10
while l < 11:
  print( l ,"jk")
  l -= 1
"""

# printing odd numbers

i = 1
while i <= 50:
   if (i%2 == 0):
      i += 1
      continue
   print(i)
   i += 1

# printing even numbers

i = 1
while i <= 50:
   if (i%2 == 1):
      i += 1
      continue
   print(i)
   i += 1

i = 1
while i < 10:
   if(i == 4):
      break
   print(i)
   i += 1   

sports = ["Cricket" , "Baseball" , "tenis" , "football"]

for value in sports:
   print(value)

atup = (4 ,7 , 8 , 9 ,1 ,3 , 4 ,1, 0 , 7, 5)
o = int(input("enter a value: "))
idx = 0
for value in atup:
  if (value == o):
      print( o , "found at index", idx)
  idx += 1