from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest
import json


def add(request, *args, **kwargs):
    if request.method == "GET":
        try:
            request_data = json.loads(request.body)
            return JsonResponse({"answer": int(request_data["A"]) + int(request_data["B"])})
        except ValueError:
            return HttpResponseBadRequest(json.dumps({"error": "Input a number!"}))
    return HttpResponseNotAllowed(['GET'])


def subtract(request, *args, **kwargs):
    if request.method == "GET":
        try:
            request_data = json.loads(request.body)
            return JsonResponse({"answer": int(request_data["A"]) - int(request_data["B"])})
        except ValueError:
            return HttpResponseBadRequest(json.dumps({"error": "Input a number!"}))
    return HttpResponseNotAllowed(['GET'])


def multiply(request, *args, **kwargs):
    if request.method == "GET":
        try:
            request_data = json.loads(request.body)
            return JsonResponse({"answer": int(request_data["A"]) * int(request_data["B"])})
        except ValueError:
            return HttpResponseBadRequest(json.dumps({"error": "Input a number!"}))
    return HttpResponseNotAllowed(['GET'])


def divide(request, *args, **kwargs):
    if request.method == "GET":
        try:
            request_data = json.loads(request.body)
            if int(request_data["B"]) == 0:
                return HttpResponseBadRequest(json.dumps({"error": "Division by zero!"}))
            return JsonResponse({"answer": int(request_data["A"]) / int(request_data["B"])})
        except ValueError:
            return HttpResponseBadRequest(json.dumps({"error": "Input a number!"}))
    return HttpResponseNotAllowed(['GET'])
