
from rest_framework.views import APIView

from .models import Profile
from .pagination import ProfilePagination
from .renderers import  ProfilesJSONRenderer
from .serializers import  ProfileSerializer

from apps.users.permissions import IsAdminUser


# ★ ProfileListAPIView
class ProfileListView(APIView):

    # WARN Permission unset
    # permission_classes = [IsAdminUser]
    # renderer_classes = [ProfilesJSONRenderer]
    pagination_class = ProfilePagination

    def get(self, request, *args, **kwargs):
        queryset = Profile.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = ProfileSerializer(page, many=True)
        
        return paginator.get_paginated_response(serializer.data)
