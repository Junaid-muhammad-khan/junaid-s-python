# recursive function
"""
def show(n):
    if(n == 0): #this will work as a exit of loop
        return
    print(n)
    show(n-1)   # this will give it a new value to n = n-1 

show(5)
"""

def fact(n):
    if n == 1 or n == 0:
        return 1
    return fact(n-1) * n

print(fact(5))