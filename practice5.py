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

numbers = [2,3,4,5,6,2,3,4,51,62,78]

def single_line2(list):
    for items in list:
        print(items, end=" ")

single_line2(numbers)

