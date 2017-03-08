from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListCreateCompany.as_view(), name='company_list'),
    url(r'^(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyCompany.as_view(),
        name='company_detail'),
    url(r'^(?P<company_pk>\d+)/documents/$',
        views.ListCreateDocument.as_view(),
        name='document_list'),
    url(r'^(?P<company_pk>\d+)/documents/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyDocument.as_view(),
        name='document_detail'),
]
