
from enum import Enum

itemsMenu = [
    {"name" : "cheese", "price" : 3, "is_dairy" : True },
    {"name" : "milk", "price" : 6, "is_dairy" : True },
    {"name" : "eggs", "price" : 8, "is_dairy" : False },
    {"name" : "bread", "price" : 4, "is_dairy" : False }
 ]
cart = []
wallet = 0
total = 0
class Actions(Enum):
    ADD = 1
    REMOVE = 2
    DISPLAY = 3
    FIND = 4
    CHECKOUT = 5 
    EXIT = 6

def addToCart():
    itemToAdd = int(input("Select an item to add (by index): "))
    if itemsMenu[itemToAdd] in itemsMenu:
        quantityToAdd = int(input(f"How many {itemsMenu[itemToAdd]['name']}/s do you want to buy?"))
        cart.append({"name" : itemsMenu[itemToAdd]['name'], "price" : itemsMenu[itemToAdd]['price'],"quantity" : quantityToAdd, "is_dairy" : itemsMenu[itemToAdd]['is_dairy']})
        print(f"Added {itemsMenu[itemToAdd]['name']} to the cart!")
    
    print("Your cart:")
    for item in cart:
         print(f"x{item['quantity']} {item['name']}", sep=",")

def removeFromCart():
    if cart != []: 
     print("Your cart:")
     for index, item in enumerate(cart):
        print(f"{index}: x{item['quantity']} {item['name']}", sep=",")

     itemToRemove = int(input("Select an item to remove (by index): "))
     if cart[itemToRemove] in cart:
        # quantityToRemove = int(input(f"How many {cart[itemToRemove]['name']}/s do you want to remove?")) tyring to remove quantity
        print(f"removed {cart[itemToRemove]['name']} from the cart!")
        cart.pop(itemToRemove)
     
        print("Your cart:")
        for item in cart:
            print(f"x{item['quantity']} {item['name']}", sep=",")

    else:
        print("Cart is empty!")

def displayCart():
    pass

def FindItemInCart():
    pass

def Checkout():
    pass

def menu():
    
    print(f"Wallet: {wallet}$"), print(f"Total: {total}$"), print("MENU:")
    print("----------------------------------------------------------------")
    for index, item in enumerate(itemsMenu):
        
        print(f"{index}: {item['name']} - {item['price']}$", end=" | ")
    print("\n----------------------------------------------------------------")
    
    for act in Actions:
        print(f"{act.value} - {act.name}")

    user_input = Actions(int(input("select an option: ")))
    print(f"You chose to: {user_input.name}")
    return user_input




if __name__ == "__main__":
   while True:
    user_input = menu()

    if user_input == Actions.ADD:
            addToCart()

    elif user_input == Actions.REMOVE:
            removeFromCart()
        
    elif user_input == Actions.DISPLAY:
            displayCart()

    elif user_input == Actions.FIND:
        FindItemInCart()

    elif user_input == Actions.CHECKOUT:
        Checkout()
        
    elif user_input == Actions.EXIT:
        exit()

    

    
   