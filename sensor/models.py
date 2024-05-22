from django.db import models

# Create your models here.

class SensorData(models.Model):
    timestamp=models.DateTimeField()
    sensor_id=models.CharField(max_length=50)
    sensor_type=models.CharField(max_length=50)
    value=models.FloatField()
    unit=models.CharField(max_length=20)
    location=models.CharField(max_length=100)
    status=models.CharField(max_length=20)
    battery_level=models.IntegerField()
    calibration_date=models.DateTimeField()
    environment_context=models.JSONField()
    data_quality=models.CharField(max_length=20)
    
    
    def __str__(self):
        return f"{self.sensor_type} at {self.timestamp}"
