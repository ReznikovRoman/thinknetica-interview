from typing import Union
from uuid import uuid4

from .product import Product


class Cart:
    """Cart with Products"""
    def __init__(self, products: list = None):
        if products is None:
            self._products = []
        else:
            self._products = products

        self._id = str(uuid4())

    def get_products(self) -> list:
        return self._products

    def set_products(self, products: list):
        if isinstance(products, list):
            self._products = products
        else:
            print("Error! Products must be list.")

    def add_product(self, new_product: Union[Product, list]):
        """
        Adds product to the Cart

        Args:
            new_product (Product): new Product that will be added

        Returns:
            None
        """
        if isinstance(new_product, Product):
            self._products.append(new_product)
        elif isinstance(new_product, list):
            for np in new_product:
                if isinstance(np, Product):
                    self._products.append(np)
                else:
                    print("Error! product must be Product.")
        else:
            print("Error! product must be Product.")

    @property
    def _price(self):
        return sum([p.get_price() for p in self._products])

    def get_price(self) -> int:
        return self._price

    def get_id(self) -> str:
        return self._id

    def set_id(self, new_id: str):
        if isinstance(new_id, str):
            self._id = new_id
        else:
            print("Error! Cart ID must be str.")

    def print_products(self):
        """Prints all products in the Cart"""
        if self._products:
            for p in self._products:
                print(p)
        else:
            print("Cart is empty.")

    def print_products_with_indexes(self, _msg: str = None):
        """Prints all products (name: price) and their indexes"""
        if _msg is not None:
            print(_msg)

        for i, good in enumerate(self._products, 1):
            print(f"{i} - {good.get_name()} ({good.get_price()})")

    def delete_product(self, product_to_delete: Product):
        """
        Removes a given Product from the Cart

        Args:
            product_to_delete (Product): Product that will be removed

        Returns:
            None
        """
        if isinstance(product_to_delete, Product):
            if product_to_delete in self._products:
                self._products.remove(product_to_delete)
            else:
                print(f"Error! Product {product_to_delete.get_name()} is not in the Cart.")
        else:
            print("Error! product must be Product.")
        print(f"Product {product_to_delete} has been removed from the Cart!")

    def clear(self):
        """Removes all Products from the Cart"""
        self._products.clear()

    def __str__(self):
        return f"Products: {self._products}, Cart ID: {self._id}"

    def __repr__(self):
        return f"(Products: {self._products}, Cart ID: {self._id})"




