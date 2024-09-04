from django.db import models

# Create your models here.



class CandleStick(models.Model):
    x = models.DateField()
    open = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    close = models.IntegerField()



class LineChartData(models.Model):
    label = models.CharField(max_length=255)
    value = models.IntegerField()



class BarChartData(models.Model):
    label = models.CharField(max_length=255)
    value = models.IntegerField()


class PieChartData(models.Model):
    label = models.CharField(max_length=255)
    value = models.IntegerField()