from datetime import date

from .cart import Cart
from .product import Product


class Person:
    """Person with the name and the date of birth"""
    def __init__(self, name: str, date_of_birth: date):
        self._name = name
        self.__dob = date_of_birth

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        if isinstance(name, str):
            self._name = name
        else:
            print("Error! Name must be str.")

    def get_dob(self) -> date:
        return self.__dob

    def set_dob(self, dob: date):
        if isinstance(dob, date):
            self.__dob = dob
        else:
            print("Error! Date of birth must be date.")

    @property
    def _age(self):
        """Calculates person's age by a given date of birth"""
        today = date.today()
        born = self.__dob
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}"

    def __repr__(self):
        return f"(Name: {self._name}, Age: {self._age})"


class Customer(Person):
    """
    Customer in the Online Shop;
    Can add products to the Cart, buy products, see purchase history
    """
    customers = []
    customers_count = 0

    def __init__(self, name: str, date_of_birth: date, bank_account: int,
                 cart: Cart = None, owned_products: list = None):
        super(Customer, self).__init__(name, date_of_birth)
        self._bank_account = bank_account
        Customer.customers_count += 1
        Customer.customers.append(self)

        if cart is None:
            self._cart = Cart()
        else:
            self._cart = cart
        if owned_products is None:
            self._owned_products = []
        else:
            self._owned_products = owned_products

    def add_to_cart(self, products: (Product, list)):
        """
        Adds product to the Cart

        Args:
            products ((Product, list)): product(s) that will be added to the Cart

        Returns:
            None
        """
        if isinstance(products, Product):
            self._cart.add_product(products)
        elif isinstance(products, list):
            for product in products:
                if isinstance(product, Product):
                    self._cart.add_product(product)
                else:
                    print("Error! product must be Product.")
        else:
            print("Error! products must be Product or list of Product")

    def cart_checkout(self):
        """Checkout stage - user 'buys' all products from the Cart"""
        price = self._cart.get_price()
        if self._bank_account > price:
            self.withdraw(price)
            self._owned_products.extend([cart_item for cart_item in self._cart.get_products()])
            self._cart.clear()
            print("Thank you for your purchase!")
        else:
            print("Error! You don't have enough money to buy all products from the cart.")

    @classmethod
    def print_customers_count(cls):
        print(f"There are {Customer.customers_count} registered customers.")

    def get_bank_account(self) -> int:
        return self._bank_account

    def set_bank_account(self, bank_account: int):
        if isinstance(bank_account, int):
            self._bank_account = bank_account
        else:
            print("Error! Bank account must be int.")

    def deposit(self, deposit: int):
        """
        Deposits money to the user's account

        Args:
            deposit (int): deposit's amount

        Returns:
            None
        """
        if isinstance(deposit, int):
            self._bank_account += deposit
        else:
            print("Error! Deposit must be int.")

    def withdraw(self, withdrawal: int):
        """
        Withdraws money from the user's account

        Args:
            withdrawal (int): withdrawal's amount

        Returns:
            None
        """
        if isinstance(withdrawal, int):
            if self._bank_account > withdrawal:
                self._bank_account -= withdrawal
            else:
                print(f"Error! You cannot withdraw {withdrawal}. You have only {self._bank_account}")
        else:
            print("Error! Withdrawal must be int.")

    def get_cart(self) -> Cart:
        return self._cart

    def set_cart(self, cart: Cart):
        if isinstance(cart, Cart):
            self._cart = cart
        else:
            print("Error! cart must be Cart.")

    def get_owned_products(self) -> list:
        return self._owned_products

    def set_owned_products(self, owned_products: list):
        if isinstance(owned_products, list):
            self._owned_products = owned_products
        else:
            print("Error! Owned products must be list.")

    def print_owned_products(self):
        """Prints user's owned products (purchase history)"""
        if self._owned_products:
            for op in self._owned_products:
                print(op)
        else:
            print("You haven't bought anything yet.")

    def __str__(self):
        return super().__str__() + \
               f";\nCart: {self._cart.get_products()}, Owned Products: {self._owned_products}, Bank Account: {self._bank_account}"

    def __repr__(self):
        return '(' + super().__str__() \
               + f"; Cart: {self._cart.get_products()}, Owned Products: {self._owned_products}, Bank Account: {self._bank_account})"

