from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title='Blog Stack Backend',
        description='A DRF-Powered Backend For Managing And Publishing Blog Posts, Categories, And User Comments.',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('restapi/',include('app.urls')),
    path('tmpauth/',include('rest_framework.urls')),
    path('',schema_view.with_ui('swagger'),name='schema-swagger-ui'),
]