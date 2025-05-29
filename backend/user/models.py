from typing import Any, Optional
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractUser,
)
from django.db import models


class UserManager(BaseUserManager):

    use_in_migrations: bool = True

    def _create_user(self, email: str, password: Optional[str], **extra_fields: Any) -> 'User':
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
            self,
            email: str,
            password: Optional[str] = None,
            **extra_fields: Any
    ) -> 'User':
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields: Any) -> 'User':
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: list = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
