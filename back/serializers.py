from .models import ServiceModel, SecServiceModel
from rest_framework import serializers

class SecServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecServiceModel
        fields = ['id', 'service_identifier', 'service_name', 'module_status', 'operation_type', 'data_class', 'data_identifier', 'start_time', 'end_time', 'number_of_copy', 'ip_address']