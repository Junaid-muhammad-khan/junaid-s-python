dict = {
    "brand":"toyota",
    "model":"supra",
    "year":2023

}

print(dict)
print(dict["brand"])

dict0 = {
    "brand" : "honda",
    "model" : "vezel",
    "year" : 2022

}

x=dict0.keys()         
print(x)


dict1 = {
    "brand" : "honda",
    "model" : "vezel",
    "year" : 2022

}

x=dict1.values()
print(x)

dict2 = {
    "Country" : "Pakistan",
    "City" : "Karachi"
}

x = dict2.values()
dict2["resturant"] = "Biryani"
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

bin_hashim = {
    "groccery" : "floor 1st",
    "toys"     : "2nd floor",
    "medical" : "3rd floor"

}
x = bin_hashim.keys()
y = bin_hashim.values()
z = bin_hashim.items()

print(x, y , z)

thefamily = {
    "Father" : {
        "name" : "Mk",
        "age" : 35
    },
    "Mother" : {
        "name" : "H",
        "age" : 35
    },
    "Y.brother" : {
        "name" : "Ahsan",
        "age" : 16
    },
    "Big.b" : {
        "name" : "Junaid",
        "age" : 18
    }
}

print(thefamily)

father0 = {
    "name" : "Mk",
        "age" : 35
}

mother0 = {
    "name" : "Hi",
        "age" : 35
}

brother0 = {
    "name" : "donkey",
        "age" : 17
}

brother1 = {
    "name" : "Junaid",
        "age" : 18
}

thefamily0 = {
    "father" : father0,
    "mother" : mother0,
    "y.brother0" : brother0,
    "b.brother" : brother1

}

print(thefamily0)