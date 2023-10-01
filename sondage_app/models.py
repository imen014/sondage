from django.db import models

""" - Définissez des modèles pour les sondages, les questions et les choix."""

class Client(models.Model):
    nom = models.CharField(max_length=50)
    age = models.IntegerField()



class Sondage(models.Model):
    titre = models.CharField(max_length=50, default='titre par defaut')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='sondages')


class Question(models.Model):
    question_sondage = models.CharField(max_length=100)
    sondage_associer = models.ForeignKey(Sondage, on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')

class Reponse(models.Model):
    reponse_client = models.CharField(max_length=200)
    sondage = models.ForeignKey(Sondage, on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
