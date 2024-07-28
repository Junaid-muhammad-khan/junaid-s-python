def divomode(a,b):
    print(a//b)
    print(a%b)
    print (divmod(a,b)) # divmode return quotient and reminder as a tuple
    
divomode(177,10)

#OR
a = int(input())
b = int(input())
c = divmod(a,b)

print(c[0])
print(c[1])
print(c)