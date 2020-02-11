from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from api.views import RegisterUserView

from api.views import LoginUserView

router = routers.DefaultRouter()

urlpatterns = [
    url('register/', RegisterUserView.as_view(), name='register-user'),
    url(r'^login/', LoginUserView.as_view(), name="login"),
    #url('token-verify/', VerifyJwtTokenView, name='token-verify'),
]