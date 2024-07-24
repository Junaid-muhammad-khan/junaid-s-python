#Make a restarant billing syestem
# Add items short keys
# Items price
# Total amount of items
# amound paid by coustomer
# Change of amount to counstomer


# First Menu
class Resturant:
    def __init__(self):
        self.menu = {
            "1" : {"name":"Chicken biryani" , "price" : 300},
            "2" : {"name":"tikka" , "price" : 250},
            "3" : {"name":"Nihari" , "price" : 330},
            "4" : {"name":"Karachi" , "price" : 290},
            "5" : {"name":"Handi" , "price" : 330},
            "6" : {"name":"naan" , "price" : 25},
            "7" : {"name":"paratha" , "price" : 30},
            "8" : {"name":"juice" , "price" : 120}
                    }
        
    def cus_input(self):
        total = 0
        while True:
            customer = input("Enter dish: ")

            if customer == "done":
                break             
            elif customer in self.menu:
                total += self.menu[customer]["price"]
            else:
                print("Invalid")

        print(f"total sum of the dish: {total}")


resturant = Resturant()
resturant.cus_input()