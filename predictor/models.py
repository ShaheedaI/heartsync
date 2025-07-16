from djongo import models

class PatientRecord(models.Model):
    age = models.IntegerField()
    cholesterol = models.FloatField()
    blood_pressure = models.FloatField()
    max_heart_rate = models.FloatField()
    prediction = models.BooleanField()
