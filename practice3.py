# write a program to ask user to enter his 3 favourite movie and store them in a list
"""
movie1 = str(input("Enter your favorite movie : "))
movie2 = str(input("Enter your favorite movie : "))
movie3 = str(input("Enter your favorite movie : "))

movies = [movie1 , movie2, movie3]
print(movies)"""

# write a program to check if a list contains a palindrome of elements.

"""palindrome = [1,2,1]
copypalindrome = palindrome.copy()
copypalindrome.reverse()

if palindrome == copypalindrome:
    print("list is palimdrome")
else:
    print("list is not palindrome")

"""

# write a program to count students got A grade in class in tuple

"""grades = ("A" , "B" , "C" , "f" , "A")
print(grades.count("A"))

listgrade = ["A" , "C" , "B" , "f" , "A"]
listgrade.sort()
print(listgrade)
"""
"""word_meaning = {
    "table" : ("piece of furniture","List of fact and figure"), 
    "cat" : "animal"

}
print(word_meaning)
"""
# you have given a list of subjects for student. Assume one class room is required for 1 subject.how many classroom are needed by all students

"""subjects = {"html" , "css" , "java" , "jquery " , "python" , "c++","html" , "css" , "java" , "python" , "c++", }
print(len(subjects))"""

# write a program to enter marks of 3 subjects from user and store them in dictionary. start with and empty dictionary and add one by one. use subject name as key and marks as value

"""marks = {}

marks.update({str(input("Enter subject : ")) : int(input("Enter marks of subject : "))})
marks.update({str(input("Enter subject : ")) : int(input("Enter marks of subject : "))})
marks.update({str(input("Enter subject : ")) : int(input("Enter marks of subject : "))})
print(marks)"""

# Figure a way to store 9 and 9.0 as a different value in a set

a = int(9)
b = str("9.0")
aset = {a ,b}
print(aset)

# OR

aset = {9 ,"9.0"}
print(aset)

# OR

aset = {"9" ,9.0}
print(aset)

# or

aset = {
    ("int" , 9),
    ("Float" , 9.0)
    }
print(aset)