from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class SampleUserManager(BaseUserManager):
    """Sample manager for SampleUser"""
    def create_user(self, email, name, role, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            role='staff'
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class SampleUser(AbstractBaseUser):
    """Sample user model"""
    USER_ROLE_CHOICES = (
        ('staff', 'staff'),
        ('provider', 'provider'),
        ('customer', 'customer'),
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='customer')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = SampleUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_admin

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
