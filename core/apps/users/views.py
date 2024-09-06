from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

import logging

User = get_user_model()
logger = logging.getLogger(__name__)

# ★ CustomUserDetailsView
class CustomUserDetailsView(RetrieveUpdateAPIView):
    
    serializer_class = UserSerializer # {□} UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return User.objects.none()



# ★ CreateSampleUserView
class CreateSampleUserView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
    
        logger.info("create_user called") # _LOG_ ● create_user 
        User.objects.create_user(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password = data['password1'],
            role = data['role']
        )

        return Response(status=status.HTTP_201_CREATED)
        



# ★ DeleteAllUsersView
class DeleteAllUsersView(APIView):
    def delete(self, request, *args, **kwargs):

        queryset = User.objects.all()
        queryset.delete()
        
        logger.info("Deletou tudo ") # _LOG_ ★

        return Response(status=status.HTTP_204_NO_CONTENT)