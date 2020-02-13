from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from api.views import RegisterUserView

from api.views import LoginUserView

from api.views import CreateExperiment

from api.views import ExperimentViewSet

router = routers.DefaultRouter()
router.register(r'experiments', ExperimentViewSet,
                base_name='experiment')
urlpatterns = [
    url(r'^', include(router.urls)),
    url('register/', RegisterUserView.as_view(), name='register-user'),
    url(r'^login/', LoginUserView.as_view(), name="login"),
    url(r'^create-experiment', CreateExperiment.as_view, name='create-experiment'),
    # url('token-verify/', VerifyJwtTokenView, name='token-verify'),
]
