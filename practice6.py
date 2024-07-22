# with open("practice.txt","r") as p:
#     data = p.read()

# new_data = data.replace("java" , "Python")
# print(new_data)

# with open("practice.txt","w") as p:
#     data = p.write(new_data)
"""
word = input("Enter a word: ")

def check_for_word(word):
    with open("practice.txt","r") as p:
        data = p.read()
        if word in data:
            print("yes",word ,"exist")
        else:
            print("no", word,"does not exist")

check_for_word(word)
"""
word = input("Enter a word: ")
def check_for_lines(word):
    lines = 1
    data = True
    with open("practice.txt","r") as p:
        while data:
            data = p.readline()
            if word in data:
                print("yes word exist on line" , lines)
                return
            lines += 1
    return -1            
check_for_lines(word)

