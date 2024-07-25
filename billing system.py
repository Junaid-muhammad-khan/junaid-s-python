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
            "2" : {"name":"Tikka" , "price" : 250},
            "3" : {"name":"Nihari" , "price" : 330},
            "4" : {"name":"Karahi" , "price" : 550},
            "5" : {"name":"Handi" , "price" : 330},
            "6" : {"name":"Naan" , "price" : 25},
            "7" : {"name":"Paratha" , "price" : 30},
            "8" : {"name":"Juice" , "price" : 120}
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
            
        print(f"total sum of the dishes: {total}")

        amount = float(total)
        payment = float(input("Amount paid by customer: "))

        if payment >= amount:
            change = payment - amount
            print(f"The change for customer is: {change}")
            print("Thank you for ordering! Your food will be ready shortly.")

        elif payment < amount:
                remaining = amount - payment # value store in remaining
                print(f"remaining amount is: {remaining}")
                remainingpay = float(input("pay the ramaing amount: "))

                while remaining != 0:
                    remaining = remaining - remainingpay  # Update remaining amount
        
                    if remaining > 0:
                        print(f"Remaining amount is: {remaining}")
                        remainingpay = float(input("Pay the remaining amount: "))
                    
                    elif remaining < amount:
                         change = (-1) * remaining
                         print(f"Here you go your change {change}")
                         print(f"Thank you for ordering! Your food will be ready shortly.")
                         break
                    else:
                        print("Thank you for ordering! Your food will be ready shortly.")
                        break

        elif change == 0:
                return 0
        else:
            print("Thank you for ordering! Your food will be ready shortly.")



resturant = Resturant()
resturant.cus_input()