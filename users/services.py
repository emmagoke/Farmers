from django.db.utils import IntegrityError
from rest_framework import  status

from .serializers import RegisterUserSerializer

class AuthenticationService:
    @classmethod
    def create_user_service(cls, request):
        data = request.data
        try:
            serializer = RegisterUserSerializer(data=data)

            if serializer.is_valid():
                user = serializer.save()
                return dict(
                    message="Signup successfully",
                    status=status.HTTP_201_CREATED
                )

            print(serializer.errors)
            return dict(
                errors=True,
                # message=list(serializer.errors.items())[0][0] + " error."
                message=str(serializer.errors) + " error.",
                status=status.HTTP_400_BAD_REQUEST
            )
        except IntegrityError as e:
            return dict(
                errors=True,
                # message=list(serializer.errors.items())[0][0] + " error."
                message=str(e),
                status=status.HTTP_400_BAD_REQUEST
            )
