from django.contrib.auth import get_user_model
from django.db import models

from core.utils.url_shortener import available_chars, generate_alias

User = get_user_model()


# Create your models here.
class ShortenedURL(models.Model):
    alias = models.TextField()
    url = models.TextField()
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    inserted_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    @classmethod
    def create(cls, url: str, owner: User | None = None):
        return cls.objects.create(
            alias=cls.get_alias(),
            url=url,
            owner=owner,
        )

    @classmethod
    def get_alias(cls) -> str:
        current_length = 3
        while cls.objects.count() / (len(available_chars) ** current_length) >= 0.3:
            current_length += 1
        alias = generate_alias(current_length)
        while cls.objects.filter(alias=alias).exists():
            alias = generate_alias(current_length)
        return alias
