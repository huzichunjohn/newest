from django.conf.urls import url, include
from rest_framework.authtoken import views as token_views
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', token_views.obtain_auth_token),
]
