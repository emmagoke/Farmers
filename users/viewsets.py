from rest_framework import viewsets, status
from rest_framework.decorators import action

from core.response_manager import ResponseManager
from .services import  AuthenticationService


class AuthenticationViewset(viewsets.ViewSet):

    @action(
        detail=False,
        methods=["post"],
        url_path="create-user",
    )
    def create_user(self, request):
        """ """
        response = AuthenticationService.create_user_service(request)

        return ResponseManager.handle_response(
                errors=response.get("errors", None),
                message=response.get("message", None),
                status=response.get("status")
            )
