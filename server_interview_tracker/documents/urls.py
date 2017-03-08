from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^companies/$', views.ListCreateCompany.as_view(), name='company_list'),
    url(r'^companies/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyCompany.as_view(),
        name='company_detail'),
    url(r'^companies/(?P<company_pk>\d+)/documents/$',
        views.ListCreateDocument.as_view(),
        name='document_list'),
    url(r'^companies/(?P<company_pk>\d+)/documents/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyDocument.as_view(),
        name='document_detail'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]
