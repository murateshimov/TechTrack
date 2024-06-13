from django.db import models

class Equipment(models.Model):
    TYPE_CHOICES = (
        ('robot', 'Robot'),
        ('manufacturing', 'Manufacturing Equipment'),
        ('quality_control', 'Quality Control System'),
    )
    equipment_type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.model} - {self.equipment_type}"

class Data(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Data for {self.equipment.model} at {self.timestamp}"

class Alerts(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Alert on {self.timestamp} for {self.equipment.model}"
