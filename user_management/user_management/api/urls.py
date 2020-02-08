from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet

from api.views import RegisterUserView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
    url('register', RegisterUserView.as_view({'post': 'create'}))
]
