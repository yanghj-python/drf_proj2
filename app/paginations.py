from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination


# 基础分页器
class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    max_page_size = 5
    page_size_query_param = "page_size"
    page_query_param = "page"


# 偏移分页器
class MyLimitPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 5


# 游标分页器 (加密)
class MyCoursePagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 5
    ordering = "-price"
