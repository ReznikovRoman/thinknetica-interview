from typing import Union


class Product:
    """Product in the Shop"""
    products_count = 0

    def __init__(self, name: str, price: int):
        self._name = name
        self._price = price
        Product.products_count += 1

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        if isinstance(name, str):
            self._name = name
        else:
            print("Error! Name must be int.")

    def get_price(self) -> Union[int, float]:
        return self._price

    def set_price(self, price):
        if isinstance(price, (int, float)):
            self._price = price
        else:
            print("Error! Price must be int or float.")

    def __str__(self):
        return f"{self._name}: {self._price}"

    def __repr__(self):
        return f"(Name: {self._name}, Price: {self._price})"

