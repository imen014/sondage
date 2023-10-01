from django.shortcuts import render
from django.http import HttpResponse
from sondage_app.models import Sondage, Client, Question, Reponse

"""- Implémentez des vues pour afficher la liste des sondages,
 les détails d'un sondage et permettre 
aux utilisateurs de voter pour une option."""

def creation_client(request):
    client1 = Client.objects.create(nom="samir", age=25)
    client2 = Client.objects.create(nom="amjed", age=26)
    client3 = Client.objects.create(nom="taher", age=27)
    return render(request,
                  'sondage_app/client_valide.html',
                  {'client1':client1, 'client2':client2, 'client3':client3})

def afficher_clients(request):
    clients = Client.objects.all()
    return render(request, 'sondage_app/clients.html', {'clients': clients})

def supprimer_client(request, id):
    client_suppr = Client.objects.get(id=id)
    client_suppr.delete()
    return render(request, 'sondage_app/valider_suppression.html')

def modifier_client(request, id):
    client_modif = Client.objects.get(id=id)
    client_modif.nom = "rami"
    client_modif.age = 26
    return render(request, 'sondage_app/modification_client.html',{'client_modif':client_modif})


def creation_sondage(request):
    client = Client.objects.get(pk=35)
    sondage = Sondage.objects.create(titre='sondage7', client=client)
    return render(request, 'sondage_app/sondage_valide.html', {'sondage':sondage})

def afficher_liste_sondage(request):
    sondages = Sondage.objects.all()
    return render(request, 
           'sondage_app/sondages.html',
           {'sondages':sondages})

def modifier_sondage(request, id):
    sondage = Sondage.objects.get(id=id)
    client = Client.objects.get(pk=32)
    sondage.titre = "sondage5"
    sondage.client = client
    sondage.save()
    return render(request, 'sondage_app/modification_sondage.html', {'sondage':sondage})

def afficher_details_sondage(request, id=id):
    sondage = Sondage.objects.get(id=id)
    return render(request, 'sondage_app/afficher_details_sondage.html', {'sondage':sondage})

def create_question(request):
    sondage = Sondage.objects.get(pk=1)
    question = Question.objects.create(question_sondage="À quelle fréquence faites-vous de l'exercice chaque semaine ?", sondage_associer=sondage)
    return render(request, "sondage_app/validation_question.html", {'question':question})

def afficher_liste_question(request):
    questions = Question.objects.all()
    return render(request, 'sondage_app/liste_question.html', {'questions':questions})

def modifier_question(request):
    question = Question.objects.get(pk=2)
    question.question_sondage = "Quelle amélioration suggéreriez-vous pour notre site web ?"
    question.save()
    return render(request, 'sondage_app/modification_question.html', {'question':question})

def supprimer_question(request):
    question = Question.objects.get(pk=7)
    question.delete()
    return render(request, 'sondage_app/suppression_question.html', {'eustion':question})

def creation_reponse(request):
    sondage = Sondage.objects.get(pk=1)
    client = Client.objects.get(pk=29)
    reponse = Reponse.objects.create(reponse_client="utilisation facile !", sondage=sondage , client=client)
    return render(request, 'sondage_app/validation_reponse.html', {'reponse':reponse})

def afficher_liste_reponse(request):
    reponses = Reponse.objects.all()
    return render(request, 'sondage_app/afficher_liste_reponse.html', {'reponses':reponses})

def modifier_reponse(request):
    reponse = Reponse.objects.get(id=2)
    reponse.reponse_client = "votre site est adorable !"
    reponse.save()
    return render(request, 'sondage_app/modification_reponse.html', {'reponse':reponse})

def afficher_details_reponse(request):
    reponses = Reponse.objects.all()
    return render(request, 'sondage_app/details_reponse.html', {'reponses':reponses})

def supprimer_reponse(request):
    reponse = Reponse.objects.get(pk=5)
    reponse.delete()
    return render(request, 'sondage_app/suppression_reponse.html', {'reponse':reponse})