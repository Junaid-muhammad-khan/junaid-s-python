#Make a restarant billing syestem
# Add items short keys
# Items price
# Total amount of items
# amound paid by coustomer
# Change of amount to counstomer

# Menu

print("press to select item:","item = ","price"),
print("1:","Chicken biryani =",300),
print("2:","Tikka =",250),
print("3:","Nihari =",300),
print("4:","Karahi =",550),
print("5:","Handi =",330),
print("6:","Naan =",25),
print("7:","Paratha =",30),
print("8:","Juice =",120)
print("For exiting the order type done")


class Resturant:
    def __init__(self):
        self.menu = {
            "1" : {"name":"Chicken biryani" , "price" : 300},
            "2" : {"name":"tikka" , "price" : 250},
            "3" : {"name":"Nihari" , "price" : 330},
            "4" : {"name":"Karahi" , "price" : 550},
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

        amount = float(total)
        payment = float(input("Amount paid by customer: "))

        if payment >= amount:
            change = payment - amount
            if change == 0:
                return 0
            else:
                print(f"The change for customer is: {change}")
                print("Thank you for ordering! Your food will be ready shortly.")



resturant = Resturant()
resturant.cus_input()