"""interview_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from documents import views
from rest_framework.authtoken import views as auth_views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'documents', views.DocumentViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
    #url(r'^api-token-auth/', auth_views.obtain_auth_token),
    url(r'^api/v1/', include('documents.urls', namespace='companies')),
    url(r'^api/v2/', include(router.urls, namespace='apiv2')),
]
