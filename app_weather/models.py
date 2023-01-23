from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    sunrise_time = models.DateTimeField()
    sunset_time = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'