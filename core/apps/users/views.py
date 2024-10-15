from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, AUthGroupSerializer


import logging

User = get_user_model()
logger = logging.getLogger(__name__)


# ★ ListUsersView
class ListUsersView(APIView):
    
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True) # {○} UserSerializer
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # permission_classes = (IsAuthenticated,)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


# ★ GetUserRole
class GetUserRoleView(APIView):
    
    def get(self, request, pk):
        
        user = User.objects.select_related('user_group').get(pk = pk)
        user_role = user.user_group
        serializer = AUthGroupSerializer(user_role)

        return Response(serializer.data, status=status.HTTP_200_OK)


# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


# ★ DeleteUserView
class DeleteUserView(APIView):

    logger.info("entrou na view delete pelo menos ") # [LOG] ★ 

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# ★ DeleteAllUsersView
class DeleteAllUsersView(APIView):
    def delete(self, request, *args, **kwargs):

        users = User.objects.all()
        users.delete()
        
        logger.info("Deletou tudo ") # [LOG] ★ 

        return Response(status=status.HTTP_204_NO_CONTENT)
    












