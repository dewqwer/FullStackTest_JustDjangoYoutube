from .models import Faculty
from .serializer import FacultySerializer
from django.http import HttpResponse
# from django.shortcuts import render

import os
import logging
from django.conf import settings
import datetime

# import asyncio
# import datetime
# import random
# import websockets
import json


from django.http import JsonResponse

# from .utils import realTimeNum

# from app.serializer import UserSerializer, UserSerializerWithToken
# from rest_framework import viewsets, mixins, permissions, status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth.models import User

# Create your views here.


# @api_view(['GET'])
# def current_user(request):
#     """
#     Determine the current user by their token, and return their data
#     """

#     serializer = UserSerializer(request.user)
#     print(serializer.data)
#     return Response(serializer.data)


# class CreateUser(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = UserSerializerWithToken(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserList(APIView):
#     permission_classes = (permissions.AllowAny,)


# def get(self, request, format=None):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)


# def post(self, request, format=None):
#     serializer = UserSerializerWithToken(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,
#                         status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,
#                     status=status.HTTP_400_BAD_REQUEST)


# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = (permissions.AllowAny,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     http_method_names = ['get', 'put', ]


# class UserViewSetForCreatingUser(viewsets.ModelViewSet):
#     permission_classes = (permissions.AllowAny,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializerWithToken
#     http_method_names = ['post']

from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

index_file_path = os.path.join(settings.REACT_APP_DIR, 'out',
                               'index.html')

number_file_path = os.path.join(
    settings.REACT_APP_DIR, 'src', 'showNumber.html')


def index(request):
    try:
        with open(index_file_path) as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        logging.exception('Production build of app not found')
        return HttpResponse(
            status=501,
        )


def socket(request):
    x = datetime.datetime.now()

    # x=1

    count_model = {
        "people_count": str(x),
        "num": 15,

    }

    # while(x<=10):
    #     x=x+1
    #     count_model = {
    #         "people_count": 1,
    #         "x": x,
    #         "y": 3,
    #     }

    # return HttpResponse(json.dumps(count_model), content_type="application/json")

    return JsonResponse(count_model)

    # try:
    #     with open(number_file_path) as f:
    #         # return HttpResponse(json.dumps(count_model), content_type="application/json")
    #         return HttpResponse(realTimeNum, content_type="application/json")
    # except FileNotFoundError:
    #     logging.exception('Production build of app not found')
    #     return HttpResponse(
    #         status=501,
    #     )

    # people = people_main.PeopleCounter()
    # people_count = people.people_count

    # while True:
    #     now = datetime.datetime.utcnow().isoformat()
    #         "people_count": str(people_count),
    #         "time": str(now),

    #     counter_json = json.dumps(count_model)
    #     await websocket.send(counter_json)

    # return json.dumps(count_model)


class FacultyListView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.AllowAny, )


class FacultyDetailView(RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.AllowAny, )


class FacultyCreateView(CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.IsAuthenticated, )


class FacultyUpdateView(UpdateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.IsAuthenticated, )


class FacultyDeleteView(DestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = (permissions.IsAuthenticated, )
