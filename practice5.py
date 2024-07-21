# average of 3 numbers
"""
def averageof_3(a,b,c):
    aver = (a + b + c)/2
    print(aver)

averageof_3(10,5,5)

"""
#2nd method
"""
def calc_avg(a,b,c):
    sum = a + b + c
    aver = sum / 2
    return aver

print(calc_avg(2,2,2))
print(calc_avg(2,3,3)+10)

"""

# WAF to print the lenght of a list(list is a parameter)
"""
numbers = [2,3,4,5,64,3,2,4,5]
thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

def print_len(list):
    print(len(list))
    return list

print_len(numbers)
print_len(thistuple2)

"""

# WAF to print the elements of a list in a single line(list is the parameter)
"""
numbers = [2,3,4,5,641,2,3,4,5,6,78]

def single_line(list):
    for items in range(len(list)):
        print(list[items], end = " ")
    
single_line(numbers)

"""
# 2nd
"""
numbers = [2,3,4,5,6,2,3,4,51,62,78]

def single_line2(list):
    for items in list:
        print(items, end=" ")

single_line2(numbers)

"""

# WAF to calculate factorial of n.(n is the parameter)
"""
def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        i += 1
    return fact
    
print(calc_fact(10))

"""
#again
"""
def factorail(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        i +=1 
    return fact

print(factorail(5))

"""
# again
"""
def factorail(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        i += 1
    return fact

print(factorail(10))
print(factorail(5))

"""

# again
"""
def factorail(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
        i += 1
    return fact

print(factorail(5))

"""

# again
# with while loop
"""
def factorail(n):
    fact = 1
    val = 1
    while val <= n:
        fact *= val
        val += 1
    return fact

print(factorail(5))
"""

# again
"""
def factorial(n):
    fact = 1
    val = 1         #itenator
    while val <= n:
        fact *= val
        val += 1
    return fact

print(factorial(10))
"""

# WAF to convert USD to PKR
"""
def converter(usd_val):
    pkr_val = usd_val*278
    print(usd_val,"USD =",pkr_val, "PKR")

converter(1)
"""

# WAF to take a input of a number and define it wheather it is a even or odd
"""
number = int(input("Enter a number: "))
def even(number):
    if (number%2 == 0):
        print("even")
    else:
        print("odd")

even(number)
"""

# write a recursive function to calculate the sum of first n natural numbers
"""
def sum_nat(n):
    if n == 0:
        return 0
    return sum_nat(n-1) + n

print(sum_nat(5))
"""

# Write a recursive function to print all elemnt in a list
# hint : use list & index as a parameter
"""
a = [1,2,3,4,5,6,7,8]

def print_list(list,idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list,idx+1)

print_list(a)
"""

# write a program of Fibonacci series
'''
def Fibonacci(n):
    if n==0:
        return 0
    elif n== 1:
        return 1 
    return Fibonacci(n-1) + Fibonacci(n-2)
    
print(Fibonacci(10))
'''