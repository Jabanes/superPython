
from enum import Enum

itemsMenu = [
    {"name" : "cheese", "price" : 3, "is_dairy" : True },
    {"name" : "milk", "price" : 6, "is_dairy" : True },
    {"name" : "eggs", "price" : 8, "is_dairy" : False },
    {"name" : "bread", "price" : 4, "is_dairy" : False }
 ]

cart = []
wallet = 100
total = 0
class Actions(Enum):
    ADD = 1
    REMOVE = 2
    DISPLAY = 3
    FIND = 4
    CHECKOUT = 5 
    EXIT = 6

def addToCart():
    global total
    global wallet
    itemToAdd = int(input("Select an item to add (by index): "))
    if itemsMenu[itemToAdd] in itemsMenu:
        quantityToAdd = int(input(f"How many {itemsMenu[itemToAdd]['name']}/s do you want to buy?"))
        cart.append({"name" : itemsMenu[itemToAdd]['name'], "price" : itemsMenu[itemToAdd]['price'],"quantity" : quantityToAdd, "is_dairy" : itemsMenu[itemToAdd]['is_dairy']})
        print(f"Added {itemsMenu[itemToAdd]['name']} to the cart!")

    total += itemsMenu[itemToAdd]['price'] * quantityToAdd
   
    displayCart()
    return total, wallet
    

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
     
        displayCart()

    else:
        print("Cart is empty!")

def displayCart():
    print("Your cart:")
    for index, item in enumerate(cart):
         print(f"{index}: x{item['quantity']} {item['name']}", sep=",")

def FindItemInCart():
    displayCart
    itemTofind = int(input("What item are you serching for? (by index): "))

    try:
        if cart[itemTofind] in cart:
            print(f"item found, you have x{cart[itemTofind]['quantity']} {cart[itemTofind]['name']}!")
    except IndexError:
        print("Item was not found!")

       


def Checkout():
    global cart
    global wallet
    global total
    toContinue = True
    print(f"wallet: {wallet}")
    print(f"total: {total}")
    proceed = input("Do you want to checkout(y/n)?: ")
    proceed.lower
    while toContinue:
        
        if proceed == "y" and total == 0:
            print("You didnt buy anything...")
            return

        elif proceed == "y":
            if wallet >= total:
                wallet -= total
                print("thank you for buying!")
                print(f"You have {wallet}$ left in your wallet!")
                cart = []
                total = 0
                return
                
            else:
                print("Sorry, insufficent funds... maybe remove some items from your cart?")
                return
        
        elif proceed == "n":
            print("Cya!")
            toContinue = False
            return
        else:
            print("Invalid option")
            proceed = input("Do you want to checkout(y/n)?: ").lower

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

    

    
   