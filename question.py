for i in range(1 ,int(input())+1):
    print(int((10**i-1)/9)**2)
    
#     The code snippet you’ve provided generates a sequence of squared numbers formed by digits composed entirely of the digit '1'. Here's a step-by-step explanation:

# for i in range(1, int(input()) + 1):

# This loop iterates from 1 to a number n, where n is provided by the user input. So if the user inputs 3, the loop will run with i taking values 1, 2, and 3.
# 10**i - 1

# This expression calculates a number composed of i digits all being 9. For example:
# When i = 1, 10**1 - 1 results in 9.
# When i = 2, 10**2 - 1 results in 99.
# When i = 3, 10**3 - 1 results in 999.
# (10**i - 1) / 9

# Dividing 10**i - 1 by 9 converts the number of 9s into a number composed of i digits all being 1. For example:
# For i = 1, (10**1 - 1) / 9 results in 1.
# For i = 2, (10**2 - 1) / 9 results in 11.
# For i = 3, (10**3 - 1) / 9 results in 111.
# int((10**i - 1) / 9)

# This converts the result to an integer (which is not strictly necessary here, but it makes sure the result is an integer).
# ** 2

# Finally, squaring this integer.
# So, the output of the program will be:

# When i = 1: 
# 1
# 2
# =
# 1
# 1 
# 2
#  =1
# When i = 2: 
# 1
# 1
# 2
# =
# 121
# 11 
# 2
#  =121
# When i = 3: 
# 11
# 1
# 2
# =
# 12321
# 111 
# 2
#  =12321
# And so on.
# In summary, this program prints the squares of numbers made entirely of 1s, with increasing lengths, based on the user input. For an input of 3, the output would be: