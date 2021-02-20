from .product import Product


class Shop:
    """Shop where users can buy Products"""
    shops = []

    def __init__(self):
        self._products = []
        self._shop_id = len(Shop.shops) + 1
        Shop.shops.append(self)

    def get_products(self) -> list:
        return self._products

    def set_products(self, new_products: list):
        if isinstance(new_products, list):
            self._products = new_products
        else:
            print("Error! Goods must be list.")

    def add_product(self, new_product: Product):
        """
        Adds a product to the Shop

        Args:
            new_product (Product): new Product that will be added

        Returns:
            None
        """
        if isinstance(new_product, Product):
            self._products.append(new_product)
        else:
            print("Error! product must be Product.")

    def remove_product(self, product: Product):
        """
        Removes a given product from the Shop

        Args:
            product (Product): product that will be removed

        Returns:
            None
        """
        if isinstance(product, Product):
            if product in self._products:
                self._products.remove(product)
            else:
                print(f"Error!Product {product.get_name()} is not in goods. ")
        else:
            print("Error! product must be Product.")

    def get_id(self) -> int:
        return self._shop_id

    def set_id(self, new_id: int):
        if isinstance(new_id, int):
            self._shop_id = new_id
        else:
            print("Error! Shop ID must be int.")

    def print_products(self):
        if len(self._products) > 0:
            for p in self._products:
                print(p)
        else:
            print("There are no products in the shop at the moment.")

    def print_products_with_indexes(self, _msg: str = None):
        """Prints all products (name: price) and their indexes"""
        if _msg is not None:
            print(_msg)

        for i, good in enumerate(self._products, 1):
            print(f"{i} - {good.get_name()} ({good.get_price()})")

    def __str__(self):
        return f"Goods: {self._products}; \nShop ID: {self._shop_id}"

    def __repr__(self):
        return f"(Goods: {self._products}; Shop ID: {self._shop_id})"




