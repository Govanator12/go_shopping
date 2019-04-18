def add(cart):
    item = input('What would you like to add?: ')
    item = item.title().strip()

    try:
        price = float(input('How much does it cost?: '))
    except:
        print('Error: Please enter a real number')
        return

    cart[item] = price
    print(f'{item} added to the cart\n')

def delete(cart):
    item = input('What would you like to delete?: ')
    item = item.title().strip()

    try:
        del cart[item]
        print(f'{item} removed from cart\n')
    except:
        print(f'{item} not found in cart\n')

def show(cart):
    print('\nHeres whats in your cart:')
    print('-----------------------------')

    for item, price in cart.items():
        print(f'{item}\t ${price}')

def createCart(carts, current_cart):
    ans = input('What do you want to call your new shopping cart?: ')
    ans = ans.title().strip()
    carts[ans] = ''
    selectCart(carts, current_cart)
    return ans

def selectCart(carts, current_cart):
    print('Here are your current carts:')
    print('-------------------------------')
    for name in carts.keys():
        print(name)

    ans = input('\nPlease enter the name of the cart you would like to select: ')
    ans = ans.title().strip()

    try:
        current_cart = carts[ans]
    except:
        print('Please eneter a valid cart name')

def deleteCart(carts, current_cart):
    print('Here are your current carts:')
    print('-------------------------------')
    for name in carts.keys():
        print(name)

    ans = input('\nPlease enter the name of the cart you would like to delete: ')
    ans = ans.title().strip()

    if carts[ans] == current_cart:
        print("Cannot delete the current cart")
    else:
        try:
            del carts[ans]
            print('Cart deleted')
        except:
            print('-1 deletion failed')

def goShopping():
    carts = {}

    current_cart = createCart(carts)

    while True:
        ans = input("Please choose an option form below\n 1. Add an item\n 2. Remove an item\n 3. Show current cart\n 4. Create a new cart \n 5. Select a new current cart\n 6. Delete a cart\n 7. Quit\n")

        if ans == '1':
            add(current_cart)

        elif ans == '2':
            delete(current_cart)

        elif ans == '3':
            show(current_cart)

        elif ans == '4':
            createCart(carts)

        elif ans == '5':
            selectCart(carts, current_cart)

        elif ans == '6':
            deleteCart(carts, current_cart)

        elif ans == '7':
            break

        else:
            print('Please choose one of the options presented\n')

    print('\nThanks for shopping with us!')
    print('--------------------------------')
    for cart in carts.values():

        print('ITEM\t\t PRICE\n')
        for item, price in cart.items():
            print(f'{item.title()}\t\t ${price}')
        print('---------------------------------')
        print(f'Total:\t\t ${sum(cart.values())}')

goShopping()
