from django.contrib.auth.models import User
from . import models
from . import serializers
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from documents.permissions import IsOwnerOrReadOnly
#from rest_framework import permissions

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ListCreateCompany(generics.ListCreateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDestroyCompany(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = (IsOwnerOrReadOnly,)


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
