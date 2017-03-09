from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^companies/$', views.ListCreateCompany.as_view(), name='company-list'),
    url(r'^companies/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyCompany.as_view(),
        name='company-detail'),
    url(r'^companies/(?P<company_pk>\d+)/documents/$',
        views.ListCreateDocument.as_view(),
        name='document-list'),
    url(r'^companies/(?P<company_pk>\d+)/documents/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyDocument.as_view(),
        name='document-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]
