a = ("orange","banana","apple" , "apple")
b = list(a)          # here we will convert a tuple in a list for updating element in it                
b[1] = "dates"
a = tuple(b)         # again converted to tuple 
print(a)

honda = ("civic","vezel","swift")
b = list(honda)
b[2] = "city"        # replaced a elemet
honda = tuple(b)
print(honda)

toyota = ("fortuner","corolla")
d = list(toyota)
d.append("supra")    # added a element
toyota = tuple(d)
print(toyota)


family = ("father","mother","big B")
e = list(family)
e.append("small brother")   # added a element
family = tuple(e)
print(family)


family2 = ("father","mother","big B", "pet cat")
f = list(family2)
f.append("small brother")   # added and removed a element
f.remove("pet cat")
family2= tuple(f)
print(family2)

thistuple0 = ("apple", "banana", "cherry")
print(len(thistuple0))          # length of tuple

tuple1 = ("apple", "banana", "cherry")  # can store any type of data
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1 , tuple2 , tuple3)

mytuple = ("apple", "banana", "cherry") # can find type of it
print(type(mytuple))

thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[1])

thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple2[2:5])

# tuple and list are same almost 90% is same
