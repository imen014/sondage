from django.contrib import admin
from sondage_app.models import Client, Sondage, Question, Reponse


class SondageAdmin(admin.ModelAdmin):
    list_display = ('titre', 'client')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'age')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_sondage', 'sondage_associer')

class ReponseAdmin(admin.ModelAdmin):
    list_display = ('reponse_client', 'sondage', 'client')
    

admin.site.register(Client, ClientAdmin)
admin.site.register(Sondage, SondageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Reponse, ReponseAdmin)