from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)


class ShopLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 6

class ShopPageNumberPagination(PageNumberPagination):
    page_size = 2