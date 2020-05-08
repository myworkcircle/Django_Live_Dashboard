from django.db import models

class Rooms(models.Model):
    vacancy = models.IntegerField()
    icu = models.IntegerField()
    endoscopy = models.IntegerField()
    cardio = models.IntegerField(default=None)
    neuro = models.IntegerField(default=None)
    Doctor_rating = models.IntegerField()
    

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    number_of_Rooms = models.ForeignKey('Rooms', on_delete=models.CASCADE)
    number_of_ambulance = models.IntegerField()
    patients = models.IntegerField()
    recovered_patients = models.IntegerField()

