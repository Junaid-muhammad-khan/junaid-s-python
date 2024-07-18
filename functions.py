def even(number):
    if number%2 == 0:
        print("true")
    else:
        print("false")

even(2)

def family(name):
    print("Mr." , name)

family("Junaid")
family("ahsan_gorilla")

def my_function(*kids): #If the number of arguments is unknown, add a * before the parameter name:
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid): #If the number of keyword arguments is unknown, add a double ** before the parameter name:
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def add_to_list(number):
   a = [1,2,3,4]
   a.append(number)
   print(a)

add_to_list(5)

def index_in_list():
   b = [1, 2, 3, 4, 5]
   for index, lists in enumerate(b):  
    print(lists, "is at", index)
   

index_in_list()

def remove_from_list(number):
   number = range(10)
   b = [number]
   print(b)

remove_from_list(10)
   
def max_of_two(x,y):
   if x > y:
      return x
   return y

def max_of_three(x,y,z):
   return max_of_two(x,max_of_two(y,z))

v = max_of_three(4,6,7)
print(v)

def multipy(numbers):
   total = 1
   for x in numbers:
      total *= x
   return total
   
i = multipy([1,2,3,])
print(i)

def check_typr(year):
   assert type(year) == int , "year is not valid or its not interger"
   print("succseed")
   return True

check_typr(2002)

# Generate a program using func that add int characters within sets list or tuple

def add_int(numbers0):
   total = 0
   for x in numbers0:
      total += x
   return total
   
g = add_int([5,4,3,2])
print(g)

def add_int(numbers):
   """Calculates the sum of a list of integers."""
   total = sum(numbers)
   return total
   
g = add_int([5,4,13,2])
print(g)

age = int(input("Enter your age "))

if age == 0:
      print("Newbie")
elif age < 5:
      print("small little baby")
elif age < 18:
      print("high school kid")
elif age < 40:
      print("a man with earning and struggles")
elif age < 70:
      print("relaxing")
else:
      print("dead") 

