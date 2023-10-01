"""
URL configuration for sondage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sondage_app.views import  creation_client, afficher_clients, supprimer_client, modifier_client , creation_sondage, afficher_liste_sondage, modifier_sondage, afficher_details_sondage, create_question, afficher_liste_question, modifier_question, supprimer_question, creation_reponse, afficher_liste_reponse, modifier_reponse, afficher_details_reponse, supprimer_reponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('creation_client/', creation_client),
    path('afficher_clients', afficher_clients, name='afficher-client'),
    path('supprimer_client/<int:id>/supprimer', supprimer_client),
    path('modifier_client/<int:id>/modifier', modifier_client),
    path('creation_sondage/', creation_sondage),
    path('afficher_liste_sondage/', afficher_liste_sondage , name = 'liste-sondages'),
    path('modifier_sondage/<int:id>/change', modifier_sondage),
    path('afficher_details_sondage/<int:id>/', afficher_details_sondage, name='details-sondage'),
    path('create_question/', create_question),
    path('afficher_liste_question/', afficher_liste_question, name="liste-question"),
    path('modifier_question/', modifier_question, name="modifier-question"),
    path('supprimer_question/', supprimer_question),
    path('creation_reponse/', creation_reponse, name='creation-reponse'),
    path('afficher_liste_reponse/', afficher_liste_reponse, name='liste-reponse'),
    path('modifier_reponse/', modifier_reponse, name='modifier-reponse'),
    path('afficher_details_reponse/', afficher_details_reponse),
    path('supprimer_reponse/', supprimer_reponse),
]
