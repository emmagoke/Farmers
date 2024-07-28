from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from core.response_manager import ResponseManager
from .services import FarmerService


class FarmersViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(
        detail=False,
        methods=["post"],
        url_path="create",
    )
    def create_farmers(self, request):
        response = FarmerService.create_farmer_service(request)

        return ResponseManager.handle_response(
                errors=response.get("errors", None),
                message=response.get("message", None),
                status=response.get("status"),
                data=response.get("data", None)
            )
    
    @action(
        detail=False,
        methods=["get"],
        url_path="list",
    )
    def get_farmers(self, request):
        response = FarmerService.get_farmer_service(request)

        return ResponseManager.paginate_response(
            queryset=response.get("queryset"),
            request=request,
            serializer_=response.get("serializer_"),
        )
