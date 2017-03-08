# from django.shortcuts import render
#from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from . import models
from . import serializers
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404

# class ListDocuments(APIView):
#     def get(self, request, format=None):
#         documents = Document.objects.all()
#         #many=True tells serializer to pass in multiple objects
#         serializer = DocumentSerializer(documents, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = DocumentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class ListCreateCompany(generics.ListCreateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class RetrieveUpdateDestroyCompany(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class ListCreateDocument(generics.ListCreateAPIView):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer

    def get_queryset(self):
        return self.queryset.filter(company_id=self.kwargs.get('company_pk'))

    def perform_create(self, serializer):
        company = get_object_or_404(
            models.Company, pk=self.kwargs.get('course_pk'))
        serializer.save(company=company)


class RetrieveUpdateDestroyDocument(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer

    def get_queryset(self):
        return self.queryset.filter(company_id=self.kwargs.get('company_pk'))

    #get a single object to get a single document
    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            company_id = self.kwargs.get('company_pk'),
            pk=self.kwargs.get('pk')
        )
