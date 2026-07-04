from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

from .models import CarMake, CarModel
from .populate import initiate

import json
import logging

logger = logging.getLogger(__name__)


# ---------------- LOGIN ----------------
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)

    response = {"userName": username}

    if user is not None:
        login(request, user)
        response = {
            "userName": username,
            "status": "Authenticated"
        }

    return JsonResponse(response)


# ---------------- LOGOUT ----------------
def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})


# ---------------- REGISTER ----------------
@csrf_exempt
def registration(request):

    data = json.loads(request.body)

    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "userName": username,
            "error": "Already Registered"
        })

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email
    )

    login(request, user)

    return JsonResponse({
        "userName": username,
        "status": "Authenticated"
    })


# ---------------- GET CARS ----------------
def get_cars(request):

    count = CarMake.objects.count()

    if count == 0:
        initiate()

    car_models = CarModel.objects.select_related('car_make')

    cars = []

    for car in car_models:
        cars.append({
            "CarModel": car.name,
            "CarMake": car.car_make.name
        })

    return JsonResponse({"CarModels": cars})


# ---------------- PLACEHOLDERS ----------------
def get_dealerships(request):
    return JsonResponse({"message": "Not implemented"})


def get_dealer_reviews(request, dealer_id):
    return JsonResponse({"message": "Not implemented"})


def get_dealer_details(request, dealer_id):
    return JsonResponse({"message": "Not implemented"})


def add_review(request):
    return JsonResponse({"message": "Not implemented"})