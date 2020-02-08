from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from rest_framework import viewsets, status

from api.serializers import UserSerializer
from rest_framework.decorators import permission_classes
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


@permission_classes((AllowAny,))
class RegisterUserView(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # Validate that the password is correct
        try:
            validate_password(request.data['password'])
        except Exception as e:
            resp = JsonResponse({'success': False, 'error': str(e)})
            resp.status_code = 400
            return resp

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
