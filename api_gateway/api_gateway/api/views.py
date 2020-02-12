from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.utils import json
from rest_framework.views import APIView

from api.services import user_login

from api.services import record_experiment


class RegisterUserView(APIView):

    def post(self, request, path="/", format=None):
        print(request, path, format)


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
