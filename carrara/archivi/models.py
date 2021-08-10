from django.db import models
from django.conf import settings # new
import datetime
from django.urls import reverse










# Create your models here.
class Pratica(models.Model):
    origine 			= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    tipo 				= models.CharField(max_length=80, blank=True, null=True)  # Field name made lowercase.
    istruttoria 		= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    pos 				= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    #data_prot_gen       = models.CharField("Data prot. gen.",max_length=20, null=True,blank=True)
    data_prot_gen 	    = models.DateField("Data prot. gen.", null=True,blank=True)  # Field name made lowercase.
    prot_gen 			= models.CharField("Protocollo gen.",max_length=30, blank=True, null=True)  # Field name made lowercase.
    prot_urb 			= models.CharField("Prot. Urb./SUAP",max_length=30, blank=True, null=True)  # Field name made lowercase.
    num_atto 			= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    #data_atto           = models.CharField("Data atto", max_length=20, null=True,blank=True)
    data_atto 			= models.DateField("Data atto", null=True,blank=True)  # Field name made lowercase.
    atto 				= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    richiedente 		= models.CharField(max_length=80, blank=True, null=True)  # Field name made lowercase.
    l_nasc 				= models.CharField("Luogo di nascita",max_length=30, blank=True, null=True)  # Field name made lowercase.
    #d_nasc              = models.CharField("Data di nascita", max_length=20, null=True,blank=True)
    d_nasc 				= models.DateField("Data di nascita", null=True,blank=True) # Field name made lowercase.
    citta 				= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    residenza 			= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_fisc 			= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    oggetto 			= models.TextField( blank=True, null=True)  # Field name made lowercase.
    ubicazione 			= models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    fg 					= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    mapp 				= models.CharField(max_length=70, blank=True, null=True)  # Field name made lowercase.
    com_edil 			= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    #data_ce             = models.CharField("Data comm edil", max_length=20, null=True,blank=True)
    data_ce     		= models.DateField("Data comm edil", null=True,blank=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    tecnico 			= models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    data_crea           = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    data_mod            = models.DateTimeField(auto_now=True,blank=True,null=True)


    
    class Meta:
        verbose_name_plural ='Pratiche'
        fieldLabels: [
            ("data_prot_gen", "Data protocollo"),
            ("prot_gen", "Protocollo generale"),
          
        ]


    
    def __str__(self):
        return str(self.id) + ' ' + str(self.richiedente)


# allegati alla pratica

class Allegato(models.Model):

    nome            = models.CharField('nome file', null=True,blank=True, max_length=120)
    pratica         = models.ForeignKey('Pratica',null=True,blank=True, on_delete=models.CASCADE)
    doc             = models.FileField(max_length=254, null=True,blank=True, upload_to='documents/%Y/%m/%d')

    class Meta:
        verbose_name_plural = 'Allegati'

    def __str__(self):
        return self.nome
    
'''
class Contact(models.Model):
  name = models.CharField(max_length=122)
  email = models.EmailField(max_length=120)
  desc = models.TextField()
  date = models.DateField()
  # code to show name of the person who sent you the message
  def _str_(self):
    return self.name
'''