from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager,
                                        PermissionsMixin, Permission, Group)


class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, password: str, first_name: str = ' ', last_name: str = ' '):
        if not email:
            raise ValueError("Users must have an email address!")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email: str, password: str, first_name: str, last_name: str):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_manager(self, email: str, password: str, first_name: str, last_name: str):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = True
        Group.objects.get(name='managers').user_set.add(user)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, first_name: str, last_name: str):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

    def get_or_create(self, email, password=None):
        created = True
        try:
            user = self.get(
                email=self.normalize_email(email),
            )
            created = False
        except CustomUser.DoesNotExist:
            user = self.create_user(
                email=self.normalize_email(email),
                password=password
            )
        return user, created


class CustomUser(AbstractUser, PermissionsMixin):
    # required fields
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = None
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # login parameter
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def get_all_permissions(self, obj=None):
        if self.is_superuser:
            return Permission.objects.all()
        return Permission.objects.filter(group__user=self)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        if perm in self.get_all_permissions() or perm in self.get_group_permissions():
            return True
        return False

    def has_module_perms(self, app_label):
        return True

