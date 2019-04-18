# have a class called cart that retains items and has methods to add, remove, and show

# step #1: create the cart class
class Cart():
    # when instantiated, cart object should define empty list for items
    def __init__(self, name='My Cart'):
        self.cart_name = name
        self.items = []


    # create a method to show cart
    def showCart(self):
        if not self.items:
            print('Cart is currently empty')
        else:
            print("Here's whats in your cart")
            print('---------------------------')

            count = 1
            for item in self.items:
                print(f'{count}. {item}')
                count += 1


    # create a method to add to cart
    def addToCart(self):
        ans = input('What would you like to add?')
        self.items.append(ans.title().strip)

        print(f'{item_to_add.title().strip()} added to your cart')

    # create a method to remove from cart
    def removeFromCart(self):
        if not self.items:
            showCart()
            ans = input('Please enter the number you want to remove: ')
            item_to_remove = self.items[ans - 1]
        try:
            self.items.remove(item_to_remove)
        except:
            print('Removal failed')
            return -1

        print(f'{item_to_remove.title().strip()} removed from cart')
        return 0

# create instance of cart object with empty list

my_cart = Cart("Steve's Cart")

# start the while loop until user quits
while True:
    # ask for input
    print('Please choose an option from the menu: ')
    print('---------------------------------------')
    print('1. Add item to cart')
    print('2. Remove an item from the cart')
    print('3. Show items in cart')
    print('4. Quit')

    ans = input()

    if ans == '1':
        my_cart.addToCart(var)

    elif ans == '2':
        my_cart.removeFromCart()

    elif ans == '3':
        my_cart.showCart()

    elif ans == '4':
        print('Thanks for shopping with Steve!')
        break

    else:
        print('Please select a valid option from the menu')



    # base case

    # ask if they would like to add, remove, show, perform steps using cart methods
    
