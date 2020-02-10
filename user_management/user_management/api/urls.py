from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet

from api.views import RegisterUserView
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
    url('register', RegisterUserView.as_view({'post': 'create'})),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]
