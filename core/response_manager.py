from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ResponseManager:
    """
    Class that handles various http code response messages
    """
    @staticmethod
    def handle_response(
            message: str = "", data: dict = None, status: int = 200, errors: bool = False, count=None,
            next=None, previous=None) -> Response:
        if data is None:
            data = []
        if errors:
            return Response({"errors": errors, "message": message, "data": data}, status=status)
        if count:
            return Response(
                OrderedDict(
                    [
                        ("count", count),
                        ("next", next),
                        ("previous", previous),
                        ("status", status),
                        ("message", message),
                        ("data", data),
                    ]
                ))
        return Response({"data": data, "message": message}, status=status)
    
    @staticmethod
    def handle_paginated_response(
        paginator_instance: PageNumberPagination = PageNumberPagination(), data=None
    ) -> Response:
        if data is None:
            data = {}
        return paginator_instance.get_paginated_response(data)

    @staticmethod
    def paginate_response(
        queryset, request, serializer_=None, page_size=10, paginator=CustomPagination
    ):
        paginator_instance = paginator()
        paginator_instance.page_size = page_size
        if not serializer_:
            return ResponseManager.handle_paginated_response(
                paginator_instance,
                paginator_instance.paginate_queryset(queryset, request),
            )
        return ResponseManager.handle_paginated_response(
            paginator_instance,
            serializer_(
                paginator_instance.paginate_queryset(queryset, request), many=True
            ).data,
        )
