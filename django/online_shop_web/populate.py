from typing import Callable
from functools import wraps


def handle_integrity_error(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IntegrityError:
            pass
    return wrapper


def add_model_perms_to_group(app_label: str, model_name: str, group_name):
    content_type = ContentType.objects.get(app_label=app_label, model=model_name.lower())
    perms = Permission.objects.filter(content_type=content_type)
    group = Group.objects.get_or_create(name=group_name)[0]

    for perm in perms:
        group.permissions.add(perm)


def create_groups():
    add_model_perms_to_group(app_label='products', model_name='product', group_name='managers')


@handle_integrity_error
def create_customers():
    user_1 = CustomUser.objects.create_user('user1@gmail.com', 'test')
    user_2 = CustomUser.objects.create_user('user2@gmail.com', 'test')


@handle_integrity_error
def create_managers():
    manager_1 = CustomUser.objects.create_manager('manager1@gmail.com', 'test', 'John', 'Doe')
    manager_2 = CustomUser.objects.create_manager('manager2@gmail.com', 'test', 'Mike', 'Williams')


@handle_integrity_error
def create_superusers():
    superuser_1 = CustomUser.objects.create_superuser('admin@gmail.com', 'test', 'Roman', 'Reznikov')


@handle_integrity_error
def create_products():
    product_1 = Product.objects.create(name='Apple', price=10)
    product_2 = Product.objects.create(name='Tomato', price=15)
    product_3 = Product.objects.create(name='Bread', price=20)
    product_4 = Product.objects.create(name='Phone', price=500)
    product_5 = Product.objects.create(name='TV', price=1500)
    product_6 = Product.objects.create(name='Car', price=70000)
    product_7 = Product.objects.create(name='Coke', price=2)
    product_8 = Product.objects.create(name='House', price=600000)
    product_9 = Product.objects.create(name='Pen', price=1)


def main():
    create_groups()
    print('Groups have been created...')
    create_customers()
    print('Customers have been created...')
    create_managers()
    print('Managers have been created...')
    create_superusers()
    print('Superusers have been created...')
    create_products()
    print('Products have been created...')


if __name__ == '__main__':
    import os

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_shop_web.settings')

    import django

    # Import settings
    django.setup()

    from django.contrib.auth.models import Permission, Group, ContentType
    from django.db import IntegrityError

    from products.models import Product
    from accounts.models import CustomUser

    main()
