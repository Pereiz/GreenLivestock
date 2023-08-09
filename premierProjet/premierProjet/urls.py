"""
URL configuration for premierProjet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Api pour GreenLivestock",
        default_version='v1',
        description="Ici un test pour voir comment l'api et swagger marchent ensemble",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="prime01@duck.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    #permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)


urlpatterns = [
    #----------- APP ROUTER
    path("gl/", include("home.urls")),
    #path('au/', include('authentication.urls')),

    
    #----------- SWAGGER ROUTER 
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #----------- DJOSER ROUTER
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('gl/', include('djoser.urls.jwt')),
    path('gl/', include('djoser.urls')),

    path("__debug__/", include("debug_toolbar.urls")),

    path("admin/", admin.site.urls),
    
]
