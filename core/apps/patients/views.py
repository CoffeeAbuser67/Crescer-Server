from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Patient
from .serializers import PatientSerializer, PatientBriefSerializer
from .pagination import ProfilePagination


import logging
logger = logging.getLogger(__name__)
# List and Create view for patients


# ★ PatientBriefListView
class PatientBriefListView(APIView):

    # def get(self, request):
    #     patients = Patient.objects.all()
    #     serializer = PatientSerializer(patients, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    pagination_class = ProfilePagination
    def get(self, request, *args, **kwargs) :
        queryset = Patient.objects.only('pkid', 'patient_name', 'birth_date', 'expiration_date' )
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = PatientBriefSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


#  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 


# ★ PatientCreateView
class PatientCreateView(APIView):


    def post(self, request):
        logger.info(" ● insert patient invoked ") # [LOG]  ●  insert patient 
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.info(f"Validation errors: {serializer.errors}")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )




#  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 


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
