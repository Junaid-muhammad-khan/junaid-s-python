# print number 1 to 100

"""num = 1
while num <= 100:
    print(num)
    num += 1
"""
# print number 100 to 1

"""num0 = 100
while num0 >= 1:
    print(num0)
    num0 -= 1
"""
# print a multiplication table of number n

"""
num = 1
n = int(input("Enter a number for a multiplication table : "))
while num <= 10:
    print(n*num)
    num += 1
"""
# print the elements of a list using loop
"""
alist = [1 , 3, 3, 4, 6, 7, 9, 0]
idx = 0

while idx < len(alist):
    print(alist[idx])
    idx += 1"""

# OR
"""
a = input("first: ")
b = input("second: ")
c = input("third: ")

alist = [a , b , c]
idx = 0

while idx < len(alist):
    print(alist[idx])
    idx += 1"""

# OR
"""
heros = ("iron man" , "Greem lantern" , "spiderman" , "Junsteel")
idx = 0

while idx < len(heros):
    print(heros[idx])
    idx += 1

"""

# search for a number x in following tuple
"""
tup = (1,3,4,5,6,7,8,99,0,0,5,11,3)
x = 3
num = 0
while num < len(tup):
    if (tup[num] == x):
        print("found at index", num)
    num += 1
""" 
# using for and range

# print numbers 1 to 100

"""for i in range(100):
    print(i)
"""
#print number 100 to 1
"""
for iinn in range(100 , 0 , -1):
    print(iinn)"""

# print a multiplication table

"""
n = int(input("enter a number: "))

for i in range(1 , 11):
    print(n*i)

n=int(input("num "))
for i in range(n,n*11,n):
    print(i)
"""

# WAP to find the sum of natural numbers
"""
n = 10
sum = 0

for i in range(1 ,n+1):
    sum += i
print("total sum =",sum)

n0 = 1
sum0 = 0

while n0 <= 10:
    sum0 += n0
    n0 += 1
 
print("total sum =",sum0)

"""

# WAP to find the factorial of first natural numbers

n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
 
print("factorial =",fact)

n0 = 5
fact0 = 1
for io in range( 1 , n0+1):
    fact0 *= io

print("factorial =", fact0)