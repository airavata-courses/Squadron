import uuid
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from api.services import user_login, register

from rest_framework.viewsets import GenericViewSet

from api.serializers import ExperimentSerializer

from api import services


class RegisterUserView(APIView):

    def post(self, request, path="/", format=None):

             data = json.loads(request.body)
             print(data)
             register_state = register(**data)
             resp = JsonResponse(register_state)

             if register_state['register'] == 'success':
                 resp.status_code = 200
             else:
                 resp.status_code = 400
             return resp


class LoginUserView(APIView):

    def post(self, request, path="/", format=None):

        data = json.loads(request.body)
        login_state = user_login(**data)
        resp = JsonResponse(login_state)

        if login_state['login'] == 'success':
            resp.status_code = 200
        else:
            resp.status_code = 400
        return resp


class CreateExperiment(APIView):
    def post(self, request, path="/", format=None):
        data = json.loads(request.body)
        username = data['username']
        house_area = data["house_area"]
        pincode = data["pincode"]
        months = data["months"]

        create_experiment_status = record_experiment(username, house_area, pincode, months)


class ExperimentViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    serializer_class = ExperimentSerializer
    lookup_field = 'request_id'

    def perform_create(self, serializer):
        experiment = serializer.save(request_id=str(uuid.uuid4()), status="PENDING")
        services.create_experiment(experiment)
        return

    def get_instance(self, lookup_value):
        return services.get_experiment(lookup_value)

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        lookup_value = self.kwargs[lookup_url_kwarg]
        inst = self.get_instance(lookup_value)
        return inst

    def perform_update(self, serializer):
        services.update_experiment(serializer.save(status="PENDING"))
        return

    def get_queryset(self):
        return

    def list(self, request, *args, **kwargs):
        username = request.GET["username"]
        print(username)
        # username = json.loads(request.body)['username']
        serializer = services.get_all_experiments(username)
        return Response(serializer.data)
