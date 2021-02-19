from models.shop import Shop
from models.product import Product
from models.cart import Cart


shop_1 = Shop()

user_choice = '-1'


def main():
    while user_choice != 'q':
        print('What do you want to do?')
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


if __name__ == '__main__':
    main()




