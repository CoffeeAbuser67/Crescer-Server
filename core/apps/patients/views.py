from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Patient
from .serializers import PatientSerializer, PatientBriefSerializer, PatientNoteSerializer
from .pagination import PatientPagination

from ..users.permissions import IsAdminUser





import logging
logger = logging.getLogger(__name__)
# List and Create view for patients


# ★ PatientBriefListView
class PatientBriefListView(APIView):

    pagination_class = PatientPagination
    def get(self, request, *args, **kwargs) :
        queryset = Patient.objects.only('pkid', 'patient_name', 'birth_date', 'expiration_date' ).order_by('-created_at')
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = PatientBriefSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


#  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 


# ★ PatientCreateView
class PatientCreateView(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request):
        logger.info(" ● insert patient invoked ") # [LOG] 
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )




#  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

# NOTE 
#   I need to make a separate view fot the retreat method here because 
#   the update and delete methods use custom permissions

# ★ PatientRetieveUpdateDestroyView
class PatientRetieveUpdateDestroyView(APIView):

    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 


# ★ PatientNoteUpdateView
class PatientNoteUpdateView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        serializer = PatientNoteSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)