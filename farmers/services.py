from django.db import transaction
from django.db.utils import IntegrityError
from rest_framework import  status
from datetime import date
from django.db.models import Q

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
    
    @classmethod
    def get_farmer_service(cls, request):
        user = request.user
        crops = request.query_params.get('crops', None)
        phone_number = request.query_params.get('phone_number',None)
        min_age = request.query_params.get('min_age', None)
        max_age = request.query_params.get('max_age')
        farmers = Farmer.objects.filter(user=user)

        filters = Q()

        if crops:
            filters &= Q(crops__icontains=crops) # And Condition or |= for OR
        if phone_number:
            filters &= Q(phone_number__icontains=phone_number)
        if min_age:
            today = date.today()
            date_threshold = today.replace(year=today.year - int(min_age))
            filters &= Q(birth_date__lte=date_threshold)
        if max_age:
            today = date.today()
            date_threshold = today.replace(year=today.year - int(max_age))
            filters &= Q(birth_date__gte=date_threshold)
        
        print(filters)
        farmers = farmers.filter(filters)

        serializer = FarmerSerializer(farmers, many=True)

        return dict(
            queryset=farmers,
            serializer_=FarmerSerializer,
            status=status.HTTP_200_OK
        )
