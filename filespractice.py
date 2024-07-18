data = []
f = open('int.txt' , "r")
for col in f:
    r = col.strip('\n')
    data.append(r)

f.close()
print(data)

# Writing a file

write_data = ["alpha" , "beta" , "gamma" , "delta" , "epsilon"]
with open("greekletters.txt" , "w") as g:
   for value in write_data:
       g.write(value)
       g.write('\n')

g.close()

junaid = {
    "name" : "junaid",
    "profession" : "student",
    "age" : 18
}
ahsan = {
    "name" : "Ahsan",
    "profession" : "student",
    "age" : 16
}

mk = {
    "name" : "Muhammad Khan",
    "profession" : "senior IOS Developer",
    "age" : 38
}
Mom = {
    "name" : "unknown",
    "profession" : "housewife",
    "age" : 38
}

#family = [junaid , ahsan , mk , Mom]
#with open("family" , "w") as f:
#    for details in family:
#        f.write(details)
#        f.write("\n")

#f.close()

# !!!!!! NEED TO SOLVE THIS ERROR

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

"""
#w = open("demofile.txt", "w")
#w.write("Now the file has more content!")
#w.close()            
#w = open("demofile.txt", "r")
#print(w.read())

#import os
#os.remove("demofile.txt")

"""
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

