from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, LoginSerializer
from django.contrib.auth.models import User
import json

class Registration(APIView):

    def post(self, request):
        data = request.data

        serializer = RegistrationSerializer(data=data)

        if serializer.is_valid():

            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")

            try:
                user_obj = User.objects.create_user(username=email, password=password)

            except Exception as e :

                data = {
                    "status":1,
                    "msg": str(e)
                }

                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            data = {
                "status":0,
                "msg": "User successfuly registered"
            }

            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            error = json.dumps(serializer.errors)
            data = {
                "status":1,
                "msg": str(serializer.errors)
            }

        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)




