from django.contrib import admin

from archivi.models import Pratica,Allegato

# Register your models here.
#admin.site.register(Pratica)

class PraticaAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'origine', 'richiedente', 'ubicazione']
admin.site.register(Pratica, PraticaAdmin)



class AllegatoAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'nome', 'doc']
admin.site.register(Allegato, AllegatoAdmin)


'''
class ContactAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'name', 'desc','date']
admin.site.register(Contact, ContactAdmin)
'''


