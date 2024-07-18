a = 20
b = 20
if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")
else :
    print("a and b are equal")

# short handed if..else

a = 15
b = 2
print("a") if a > b else print("b")

# And operator
# both condition ,must be true
a = 100
b = 12
c = 50

if a > b and b < c:
    print("hehehhe easy")

if a > b and b > c:  # it wont print because one statement is wrong
    print("No, wth")

# Or operator
# one statement should be true

a = 10
b = 12
c = 13

if a > b or c > b:
    print("nice")

# Not operator
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement

a = 20
b = 21
if not a > b:
    print("a is less than b")

# Nested If statement
#You can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass Statement
#  if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement

# Modulus exmaple 
# modulus will keep divinding untill it get 0 or in shorter value like 4/2=2 2/2=0 or 5/2= remmaing 1.

number = 4
if number%2 == 0:
    print("Even")
else:
    print("Odd")


number0 = 7
if number0%2 == 0:
       print("Even")
elif number0%2 != 0:
       print("Odd")
else:
       print("Neither even nor odd")


number1 = 0
if number1%2 == 0 and number1 != 0: # with this and statment we just update our code it means if number modulus to 2 == 0 then its even but also number should not be zero.
    print("even")


  
alm = 9
print("yes" if alm%2 ==0 else "no")


