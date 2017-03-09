from django.contrib.auth.models import User
from . import models
from . import serializers
from rest_framework import status, generics, viewsets
from django.shortcuts import get_object_or_404
from documents.permissions import IsOwnerOrReadOnly, IsSuperUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_list', request=request, format=format),
        'companies': reverse('company_list', request=request, format=format)
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = (IsSuperUser, IsOwnerOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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
