users_cart = {}
shopping_list = {
    'Weapon': 'Lightsaber',
    'Clothing': 'Jedi Cloak',
    'Food': 'Bantha Burger'
}

def shopping_cart(cart_func):
    print("\n Welcome to Ewok Thieves! How can we help you? \n")
    print("\n Please note that the 'cart' option will print what is in your cart and the 'show' option will print what we have in our shop \n")

    while True:
        
        user_input = input("Do you want to: Show/Add/Delete/Cart or Quit? ")

        if user_input.lower() == 'cart':
            print(users_cart)

        elif user_input.lower() == 'show':
            print(shopping_list)

        elif user_input.lower() == 'add':
            add_cart = input("Please select what you would like to add to your cart (Weapon, Clothing, Food): ")
            
            if add_cart.lower() == 'weapon':
                if 'Weapon' not in users_cart:
                    users_cart['Weapon'] = {'Lightsaber': 1}
                else:
                    if 'Weapon' in users_cart:
                        users_cart['Weapon']['Lightsaber'] += 1
                    else:
                        users_cart['Weapon']['Lightsaber'] = 1
                print("Lightsaber has been added to your cart")

            if add_cart.lower() == 'clothing':
                if 'Clothing' not in users_cart:
                    users_cart['Clothing'] = {'Jedi Cloak': 1}
                else:
                    if 'Clothing' in users_cart:
                        users_cart['Clothing']['Jedi Cloak'] += 1
                    else:
                        users_cart['Clothing']['Jedi Cloak'] = 1
                print("Jedi Cloak has been added to your cart")

            if add_cart.lower() == 'food':
                if 'Food' not in users_cart:
                    users_cart['Food'] = {'Bantha Burger': 1}
                else:
                    if 'Food' in users_cart:
                        users_cart['Food']['Bantha Burger'] += 1
                    else:
                        users_cart['Food']['Bantha Burger'] = 1
                print("Bantha Burger has been added to your cart")

        elif user_input.lower() == 'delete':
            print(users_cart)
            remove_cart = input("Please select what you would like to remove from your cart (Weapon, Clothing, Food): ")

            if remove_cart.lower() == 'weapon':
                if users_cart['Weapon']['Lightsaber'] == 1:
                    del users_cart['Weapon']
                    print("Lightsaber has been removed from your cart")
                elif users_cart['Weapon']['Lightsaber'] > 1:
                    users_cart['Weapon']['Lightsaber'] -= 1
                    print("Lightsaber has been removed from your cart")
                else:
                    print("Lightsaber not found in your cart")

            if remove_cart.lower() == 'clothing':
                if users_cart['Clothing']['Jedi Cloak'] == 1:
                    del users_cart['Clothing']
                    print("Jedi Cloak has been removed from your cart")
                elif users_cart['Clothing']['Jedi Cloak'] > 1:
                    users_cart['Clothing']['Jedi Cloak'] -= 1
                    print("Jedi Cloakcart has been removed from your cart")
                else:
                    print("Lightsaber not found in your cart")

            if remove_cart.lower() == 'food':
                if users_cart['Food']['Bantha Burger'] == 1:
                    del users_cart['Food']
                    print("Bantha Burger has been removed from your cart")
                elif users_cart['Food']['Bantha Burger'] > 1:
                    users_cart['Food']['Bantha Burger'] -= 1
                    print("Bantha Burger has been removed from your cart")
                else:
                    print("Bantha Burger not found in your cart")

        else:
            print('\n Bye bye! See you next time!\n')
            if 'Weapon' in users_cart or 'Clothing' in users_cart or 'Food' in users_cart:
                print("You left while you still had the following items in your cart:")
                if 'Weapon' in users_cart and 'Lightsaber' in users_cart['Weapon']:
                    print(f"{users_cart['Weapon']['Lightsaber']} Lightsaber")
                if 'Clothing' in users_cart and 'Jedi Cloak' in users_cart['Clothing']:
                    print(f"{users_cart['Clothing']['Jedi Cloak']} Jedi Cloak")
                if 'Food' in users_cart and 'Bantha Burger' in users_cart['Food']:
                    print(f"{users_cart['Food']['Bantha Burger']} Bantha Burger")
            else:
                print('You left the store and your cart was empty')
            break



shopping_cart(users_cart)