from datetime import date

from models.shop import Shop
from models.product import Product
from models.cart import Cart
from models.users import Person, Customer
import utils


def main():
    user_choice = '-1'
    shop_1 = Shop()
    utils.populate_shop(shop_1)
    products = shop_1.get_products()
    user_1 = Customer('Roman', date(2002, 3, 7), 1000)

    while user_choice[0] != 'q':
        print('\nAvailable options')
        print("\t\t\t\tYour current balance: ", user_1.get_bank_account())
        print("""
                1 - See all products (name: price)
                2 - Add new product
                3 - Change product's price
                4 - Change product's name
                5 - Delete product from the shop

                6 - Add product to the cart
                7 - See all products in the cart
                8 - Remove product from the cart
                9 - Buy all products in the cart
                10 - See the purchase history
                
                q - Quit the program 'Online Shop'
                """)
        user_choice = input("What do you want to do? ")
        print()

        if user_choice == '1':  # print all products in the shop
            shop_1.print_products()

        elif user_choice == '2':  # add new product
            while True:
                try:
                    product_name = input("Enter product's name: ")
                    product_price = int(input("Enter product's price: "))
                    if product_price < 0:
                        raise ValueError
                except ValueError as ve:
                    print("Please, enter correct price of the product...")
                else:
                    shop_1.add_product(Product(product_name, product_price))
                    break

        elif user_choice == '3':  # change product's price
            if len(products) > 0:
                product_to_change = utils.handle_user_input_product(
                    shop_1,
                    products,
                    "Price of which product do you want to change? "
                )

                while True:
                    try:
                        new_price = int(input("Enter new price: "))
                    except ValueError as ve:
                        print("Please, enter a number...")
                    except Exception:
                        print("Error!")
                    else:
                        break

                product_to_change.set_price(new_price)
                print("Price has been changed!")
            else:
                print("There is nothing to change - no products in the Shop yet.")

        elif user_choice == '4':  # change product's name
            if len(products) > 0:
                product_to_change = utils.handle_user_input_product(
                    shop_1,
                    products,
                    "Name of which product do you want to change? "
                )

                product_to_change.set_name(input("Enter new product's name: ").title())
                print("Product's name has been changed!")
            else:
                print("There is nothing to change - no products in the Shop yet.")

        elif user_choice == '5':  # delete product from the shop
            if len(products) > 0:
                product_to_delete = utils.handle_user_input_product(
                    shop_1,
                    products,
                    "Which product do you want to remove? "
                )

                shop_1.remove_product(product_to_delete)
                print("Product was removed from the Shop!")
            else:
                print("There is nothing to remove - no products in the Shop yet.")

        elif user_choice == '6':  # add product to the cart
            if len(products) > 0:
                while True:
                    shop_1.print_products_with_indexes("Which product do you want to add to the Cart?: ")

                    try:
                        index = int(input("Enter your choice: ")) - 1
                    except ValueError as ve:
                        print("Please, enter a number...")
                    else:
                        break

                user_1.add_to_cart(products[index])
                print(f"Product {products[index].get_name()} has been added to the Cart.")
            else:
                print("There is nothing to add to the cart - no products in the Shop yet.")

        elif user_choice == '7':  # see all products in the cart
            user_1.get_cart().print_products()

        elif user_choice == '8':  # remove product from the cart
            user_cart = user_1.get_cart()
            products_in_cart = user_cart.get_products()
            if products_in_cart:
                product_to_delete = utils.handle_user_input_product(
                    user_cart,
                    user_cart.get_products(),
                    "Which product do you want to remove? "
                )
                user_cart.delete_product(product_to_delete)
            else:
                print("There is nothing to remove - Cart is empty.")

        elif user_choice == '9':  # buy all products in the cart - checkout
            products_in_cart = user_1.get_cart().get_products()
            if len(products_in_cart) > 0:
                user_1.cart_checkout()
            else:
                print("There is nothing to buy - Cart is empty.")

        elif user_choice == '10':  # see the purchase history - print all owned products
            user_1.print_owned_products()

        elif user_choice[0] == "q":  # quit the program
            print("Thanks for using this  program!")
            break

        else:  # wrong command
            print("There is no such option.")
            continue


if __name__ == '__main__':
    main()
