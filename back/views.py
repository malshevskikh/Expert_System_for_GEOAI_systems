from django.shortcuts import render
from .models import ServiceModel, SecServiceModel
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import SecServiceSerializer
import datetime
import time

#Обновить данные в БД
@api_view(['PATCH'])
def update_data_of_service(request):
    try:
        serv_ident = request.data['service_identifier']
        serv_name = request.data['service_name']
        valid_service = SecServiceModel.objects.get(service_identifier=serv_ident, service_name = serv_name)
        print("request:", request.data)
        print("valid_service:", valid_service)
        if valid_service is not None:
            if (request.data['module_status'] == 'Отдых'):
                valid_service.module_status = SecServiceModel.ServicesStatus.REST
            elif (request.data['module_status'] == 'В работе'):
                valid_service.module_status = SecServiceModel.ServicesStatus.WORK
            valid_service.operation_type = request.data['operation_type']
            valid_service.data_class = request.data['data_class']
            valid_service.data_identifier = request.data['data_identifier']
            if (valid_service.start_time != None):
                valid_service.start_time = request.data['start_time']
            if (valid_service.end_time != None):
                valid_service.end_time = request.data['end_time']
            print('valid_service: ', valid_service.service_identifier, valid_service.service_name, valid_service.module_status, valid_service.operation_type, valid_service.data_class, valid_service.data_identifier, valid_service.start_time, valid_service.end_time)
            valid_service.save()
            return JsonResponse({'message': 'Данные обновлены'}, status=status.HTTP_204_NO_CONTENT, safe=False)
    except:
        return JsonResponse({'message': 'Исключение'}, status=status.HTTP_404_NOT_FOUND)
    return JsonResponse(status=status.HTTP_200_OK, safe=False)


#Разместить данные в БД
@api_view(['POST'])
def add_data_of_service(request):
    print("Здесь")

    if (request.data['module_status'] == 'Отдых'):
        mod_status = SecServiceModel.ServicesStatus.REST
    elif (request.data['module_status'] == 'В работе'):
        mod_status = SecServiceModel.ServicesStatus.WORK


    if request.data['number_of_copy'] is not None:
        nmb_of_cp = request.data['number_of_copy']
    else:
        nmb_of_cp = 0

    data_of_req = {
        "service_identifier": request.data['service_identifier'],
        "service_name": request.data['service_name'],
        "module_status": mod_status,
        "operation_type": request.data['operation_type'],
        "data_class": request.data['data_class'],
        "data_identifier": request.data['data_identifier'],
        "start_time": request.data['start_time'],
        "end_time": request.data['end_time'],
        "number_of_copy": nmb_of_cp,
        "ip_address": request.data['ip_address'],
    }


    print(data_of_req)
    '''
    print("service_identifier:", data_of_req["service_identifier"], type(data_of_req["service_identifier"]))
    print("service_name:", data_of_req["service_name"], type(data_of_req["service_name"]))
    print("module_status:", data_of_req["module_status"], type(data_of_req["module_status"]))
    print("operation_type:", data_of_req["operation_type"], type(data_of_req["operation_type"]))
    print("data_class:", data_of_req["data_class"], type(data_of_req["data_class"]))
    print("data_identifier:", data_of_req["data_identifier"], type(data_of_req["data_identifier"]))
    print("start_time:", data_of_req["start_time"], type(data_of_req["start_time"]))
    print("end_time:", data_of_req["end_time"], type(data_of_req["end_time"]))
    '''
    #start_time = datetime.datetime.fromtimestamp(data_of_req["st_time"])
    #end_time = datetime.datetime.fromtimestamp(data_of_req["en_time"])
    #print("diff:", end_time - start_time)
    #difference =end_time - start_time
    #seconds_in_day = 24 * 60 * 60
    serializer = SecServiceSerializer(data = data_of_req)
    print("serializer:", serializer)
    #"start_time":  	1710419160,
    #"end_time": 1710426360

    if serializer.is_valid():
        print("Всё корректно!")
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
    else:
        print("Не корректно!")
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

# Create your views here.
