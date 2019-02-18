from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        db_table='zigbee'
    id = models.AutoField(primary_key=True)
    pressure = models.CharField(max_length=2, null=False)
    pressure_flag = models.CharField(max_length=1, null=False)
    vibrance = models.CharField(max_length=5, null=False)
    vibrance_flag = models.CharField(max_length=1, null=False)
    temperature = models.CharField(max_length=4, null=False)
    temperature_flag = models.CharField(max_length=1, null=False)
    time = models.CharField(max_length=14, null=False, unique=True)

    def __repr__(self):
        return "".format(self.id, self.name)

    __str__ = __repr__
