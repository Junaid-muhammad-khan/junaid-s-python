# Sets
# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset0 = {"apple", "banana", "cherry", "apple"}
print(thisset0)                                         # Dublicates are not allowed

# in sets true = 1 and false = 0 

thisset1 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset1)

thisset2 = {"apple", "banana", "cherry", False, True, 0}
print(thisset2)

thisset3 = {"apple", "banana", "cherry"}  # cheack if banana is in set
print("banana" in thisset3)

thisset4 = {"apple", "banana", "cherry"}  # cheack if banana is not in set
print("banana" not in thisset4)

thisset5 = {"apple", "banana", "cherry"}    # add a element in set
thisset5.add("orange")   
print(thisset5)

thisset5 = {"apple", "banana", "cherry"}     # add set in set
tropical0 = {"pineapple", "mango", "papaya"}
thisset5.update(tropical0)
print(thisset5)

# adding multiple sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set5 = {"a", "b", "c"}
set6 = {1, 2, 3}
set7 = {"John", "Elena"}
set8 = {"apple", "bananas", "cherry"}

myset0 = set5| set6 | set7 |set8
print(myset0)
