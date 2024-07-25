from django.db import transaction
from django.db.utils import IntegrityError
from rest_framework import  status

from .serializers import RegisterFarmerSerializer

class FarmerService:
    @classmethod
    @transaction.atomic
    def create_farmer_service(cls, request):
        try:
            serializer = RegisterFarmerSerializer(
                data=request.data,
                many=True,
                context={'user': request.user}
            )
            if serializer.is_valid():
                farmers = serializer.save()
                print(farmers)
                return dict(
                    message="Farmers Successfully Created",
                    status=status.HTTP_201_CREATED
                )

            print(serializer.errors)
            return dict(
                errors=True,
                message=list(serializer.errors.items())[0][0] + " error.",
                status=status.HTTP_400_BAD_REQUEST
            )
        except IntegrityError as e:
            return dict(
                errors=True,
                # message=list(serializer.errors.items())[0][0] + " error."
                message=str(e),
                status=status.HTTP_400_BAD_REQUEST
            )
        
