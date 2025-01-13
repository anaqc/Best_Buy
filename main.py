import products
import store


def menu(dic_menu):
    """ This function show the user menu"""
    print("***** Store Menu *****")
    for key, dic_option in dic_menu.items():
        print(f"{key}. {dic_option['details']}")


def list_products_store(store):
    """ This function show a lis of products in the store"""
    list_products = store.get_all_products()
    print("______________________")
    for index, product in enumerate(list_products, start = 1):
        print(f"{index}. {product.show()}")
    print("______________________")


def show_total_amount(store):
    """ This function show total amount in store"""
    total_amount = 0
    for product in store.list_products:
        total_amount += product.quantity
    print("______________________")
    print(f"Total of {total_amount} items in store")
    print("______________________")


def make_order(store):
    """ This function make a order"""
    list_products_store(store)
    list_order = []
    print("When you want to finish order, enter empty text.")
    while True:
        try:
            user_choice = input("Which product # do you want? ")
            user_quantity = input("What amount do you want? ")
            total_products = store.get_all_products()
            total_payment = 0
            if (user_choice.isdigit() and 1 <= int(user_choice) <= len(total_products)
                    and user_quantity.isdigit()):
                user_choice = int(user_choice)
                user_quantity = int(user_quantity)
                product_user_choice = store.list_products[user_choice - 1]
                list_order.append((product_user_choice, user_quantity))
                print("Product added to list!")
                continue
            elif user_choice == "" and user_quantity == "" and verify_quantity(list_order):
                for product, quantity in list_order:
                    product.buy(quantity)
                print("______________________")
                print(f"Order made! Total payment: {store.order(list_order)}")
                print("______________________")
                break
            elif user_choice == "" and user_quantity == "" and not verify_quantity(list_order):
                print("Error while making order! Quantity larger than what exists")
                break
            raise ValueError("Error adding product!")
        except ValueError as e:
            print(e)

def verify_quantity(list_order) ->bool:
    """ This function verify if the product quantity in the order exist"""
    for product, quantity in list_order:
        if quantity > product.quantity:
            return False
    return True


def validate_user_input():
    """ This function validate the user input from the menu"""
    while True:
        user_input = input("Please choose a number: ")
        try:
            user_input = int(user_input)
            if  1 <= user_input <= 4:
                return user_input
            raise ValueError("Error with your choice! Try again!")
        except Exception as e:
            print(e)

def start(store):
    """ This function gek the store object as parameter and show the following menu"""
    dic_menu = {
        1: {
            "function": list_products_store,
            "details": "List all products in store"
        },
        2: {
            "function": show_total_amount,
            "details": "Show total amount in store"
        },
        3: {
            "function": make_order,
            "details": "Make an order"
        },
        4: {
            "function": exit,
            "details": "Quit"
        }
    }
    while True:
        menu(dic_menu)
        user_input = validate_user_input()
        if user_input == 4:
            dic_menu[user_input]["function"]()
        dic_menu[user_input]["function"](store)


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                   ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()

