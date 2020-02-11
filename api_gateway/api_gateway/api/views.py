from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class RegisterUserView(APIView):

    def post(self, request, path="/", format=None):
        print(request, path, format)


class LoginUserView(APIView):

    def post(self, request, path="/", format=None):
        print(request, path, format)

        resp = JsonResponse({'uploaded': False, 'error': str(e)})
        resp.status_code = 500
        return resp
