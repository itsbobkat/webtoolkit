import typing as t

from django.core.paginator import Page, Paginator
from django.db.models import Model


def get_paginated_items(
    query,
    page: int | None = None,
    page_size: int = 10,
) -> Page[Model] | None:
    page = page or 1
    if page < 0:
        return None
    p = Paginator(
        query,
        page_size,
    )
    if page > p.num_pages:
        return None
    return p.page(page)
