from typing import List, Union

from models.shop import Shop
from models.product import Product
from models.cart import Cart


def populate_shop(shop: Shop):
    shop.add_product(Product('Apple', 10))
    shop.add_product(Product('Tomato', 15))
    shop.add_product(Product('Bread', 20))
    shop.add_product(Product('Phone', 500))


def handle_user_input_product(container: Union[Shop, Cart], products: List[Product], msg: str) -> Product:
    while True:
        container.print_products_with_indexes(msg)

        try:
            product_to_change = products[int(input("Enter your choice: ")) - 1]
        except ValueError as ve:
            print("Please, enter a number...")
        except IndexError as ie:
            print("There is no product with such index, please enter index again...")
        except Exception:
            print("Error!")
        else:
            return product_to_change





