# Making a calulator with different ways
"""
num = int(input("Enter a number: "))
a = 1
while a <= 10:
    print(num, "x", a , "=" ,num * a)
    a += 1
"""
# 2nd method
"""
anum = int(input("Enter a number: "))
b = 0
for i in range(anum ,anum*11 , anum):
    print(i)
"""
# 3rd method
"""
lum = int(input("Enter a number: "))
for i in range(1 , 11):
    print(lum * i)
"""
# Find the sum of first natural numbers 
"""
n = 1
sum = 0
while n <= 5:
    sum += n
    n += 1
print(sum)
"""
# 2nd method
"""
n = 5
sum = 0
for i in range(n+1):
    sum += i
    i +=1

print(sum)
"""

# WAP to find the factorial of natural numbers
"""
n = 5
multi = 1
for i in range(1 ,n+1): # here starting value is important because range always start form 0 and here n+1 = 6 its a range means number will go 0 1 2 3 4 5
    multi *= i
    i += 1
print(multi)
"""
# 2nd
"""
n = 1
multi = 1

while n <= 5:
    multi *= n
    n += 1

print(multi)
"""