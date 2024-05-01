from django.db import models

# Create your models here.


class ServModel(models.Model):
    class ServicesStatus(models.TextChoices):
        WORK = ("WRK", "В работе")
        REST = ("RST", "Отдых")
    service_identifier = models.CharField(max_length = 255)
    service_name = models.CharField(max_length = 255)
    module_status = models.CharField(max_length=80, choices = ServicesStatus.choices, default = ServicesStatus.REST)
    operation_type = models.CharField(max_length = 255)
    data_class = models.CharField(max_length = 255)
    data_identifier = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.module_status


class ServiceModel(models.Model):
    class ServicesStatus(models.TextChoices):
        WORK = ("WRK", "В работе")
        REST = ("RST", "Отдых")
    service_identifier = models.CharField(max_length = 255)
    service_name = models.CharField(max_length = 255)
    module_status = models.CharField(max_length=80, choices = ServicesStatus.choices, default = ServicesStatus.REST)
    operation_type = models.CharField(max_length = 255)
    data_class = models.CharField(max_length = 255)
    data_identifier = models.CharField(max_length = 255)
    start_time = models.IntegerField()
    end_time = models.IntegerField()

    def __str__(self):
        return self.module_status
    

class SecServiceModel(models.Model):
    class ServicesStatus(models.TextChoices):
        WORK = ("WRK", "В работе")
        REST = ("RST", "Отдых")
    service_identifier = models.CharField(max_length = 255)
    service_name = models.CharField(max_length = 255)
    module_status = models.CharField(max_length=80, choices = ServicesStatus.choices, default = ServicesStatus.REST)
    operation_type = models.CharField(max_length = 255)
    data_class = models.CharField(max_length = 255)
    data_identifier = models.CharField(max_length = 255)
    start_time = models.BigIntegerField()
    end_time = models.BigIntegerField()
    number_of_copy = models.IntegerField(default=0)
    ip_address = models.CharField(max_length = 255, default='1.1.1.1')
    
    def __str__(self):
        return self.module_status