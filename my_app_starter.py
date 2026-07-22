# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: ____Lam Ngu______________
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: ______________Hoodie and Sweatpants___________________________
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.
class Hoodie:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def deliver(self):
        print(f"Delivering: {self.name}")
    



# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: _when typing a number that are below 0, it will print out the line_____________
#   Paste the message you see here: __A price can not be below zero____________
    def set_price(self, ammount) :
        if amount < 0 :
            print("A price can not be below zero")
        else:
            self.price = amount

# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.
class Sweatpants(Hoodie) :
    pass

# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: ______it lets different classes use the same method name________
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def deliver(self):
        print(f"Delivering: {self.name}")
        print("Packing it!")

class Sweatpants(Hoodie):
    def deliver(self):
        print(f"Delivering: {self.name}")
        print("Folding it!")

# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: _____Black Cozy Hoodie_________

item1 = Hoodie("Black Cozy Hoodie", 80)
item2 = Sweatpants("Black Cozy Sweatpants", 60)
# print(item1.name) testing
# print(item2.name) testing

# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.
class Cart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)

    def checkout(self):
        total = 0
        for item in self.items:
            item.deliver()
            total = total + item.price
        print("Total: $" + str(total))
        



# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.
class Store:
    def __init__(self):
        self.items = []

    def checkout(self):
        total = 0
        for item in self.items:
            item.deliver()
            total = total + item.price
        print("Total: $" + str(total))

# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.
store = {"1": item1, "2": item2}
cart = Cart()

# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: ____Added Black Cozy Hoodie_________
shopping = True
while shopping:
    choice = input("Pick 1, 2, or 'done': ")

    if choice in store:
        cart.items.append(store[choice])
        print("Added item!")
    elif choice == "done":
        cart.checkout()
        break
    else:
        print("Try again")

        




# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.
# first it gonna say pick the 1,2 or done
#after picking it and type done, it gonna show the item name and the cost

# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================