from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import  *
from django.views import View
from rest_framework import status
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .utility import *

@method_decorator(csrf_exempt, name='dispatch')
def info(request):
    
    # get all the drinks
    # serialize dem 
    # return json
    if request.method == 'GET':
        info = MyInfo.objects.all()
        serializer = InfoSerializer(info, many=True) #true meaning it will serialize all of dem coz we ve a list
        return JsonResponse(serializer.data[0], safe=False) # false inorder to allow non-dict objects to be serialized
    elif request.method == 'POST':
        query_dict = {}
        data = json.loads(request.body.decode("utf-8"))
        operator = data.get("operation_type")
        x_value = data.get("x")
        y_value = data.get("y")   
        get_result, operation = get_operation(operator, x_value, y_value)
        if get_result is None:
            query_dict["slackUsername"] = "olanipekun01"
            query_dict["operation_type"] = operation
            query_dict["result"] = "Incompatible types" 
            get_status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
        else:
            query_dict["slackUsername"] = "olanipekun01"
            query_dict["operation_type"] = operation
            query_dict["result"] = get_result
            get_status = status.HTTP_202_ACCEPTED     
        return JsonResponse(query_dict)