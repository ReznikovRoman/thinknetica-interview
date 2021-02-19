
class Shop:
    """Shop where users can buy Products"""
    shops = []

    def __init__(self):
        self._goods = []
        self._shop_id = len(Shop.shops) + 1
        Shop.shops.append(self)

    def get_goods(self) -> list:
        return self._goods

    def set_goods(self, new_goods: list):
        if isinstance(new_goods, list):
            self._goods = new_goods
        else:
            print("Error! Goods must be list.")

    def get_id(self) -> int:
        return self._shop_id

    def set_id(self, new_id: int):
        if isinstance(new_id, int):
            self._shop_id = new_id
        else:
            print("Error! Shop ID must be int.")

    def print_products(self):
        if len(self._goods) > 0:
            for p in self._goods:
                print(p)
        else:
            print("There are no products in the shop at the moment.")

    def print_products_with_indexes(self, _msg: str = None):
        """Prints all products (name: price) and their indexes"""
        if _msg is not None:
            print(_msg)

        for i, good in enumerate(self._goods, 1):
            print(f"{i} - {good.get_name()} ({good.get_price()})")

    def __str__(self):
        return f"Goods: {self._goods}; \nShop ID: {self._shop_id}"

    def __repr__(self):
        return f"(Goods: {self._goods}; Shop ID: {self._shop_id})"




