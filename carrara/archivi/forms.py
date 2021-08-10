from django import forms 
from django.forms import ModelForm
from .models import Pratica




class PraticaAdd(forms.ModelForm):
    
    class Meta:
        model   = Pratica
        fields  = ('__all__')

        widgets = {

            'origine'             : forms.TextInput(attrs={'class':'form-control'}),
            'tipo'                : forms.TextInput(attrs={'class':'form-control'}),
            'istruttoria'         : forms.TextInput(attrs={'class':'form-control'}),
            'pos'                 : forms.TextInput(attrs={'class':'form-control'}),
            'data_prot_gen'       : forms.DateInput(),
            'prot_gen'            : forms.TextInput(attrs={'class':'form-control'}),
            'prot_urb'            : forms.TextInput(attrs={'class':'form-control'}),
            'num_atto'            : forms.TextInput(attrs={'class':'form-control'}),
            'data_atto'           : forms.DateInput(),
            'atto'                : forms.TextInput(attrs={'class':'form-control'}),
            'richiedente'         : forms.TextInput(attrs={'class':'form-control','autofocus': True}),
            'l_nasc'              : forms.TextInput(attrs={'class':'form-control'}),
            'd_nasc'              : forms.DateInput(),
            'citta'               : forms.TextInput(attrs={'class':'form-control'}),
            'residenza'           : forms.TextInput(attrs={'class':'form-control'}),
            'cod_fisc'            : forms.TextInput(attrs={'class':'form-control'}),
            'oggetto'             : forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':15}),
            'ubicazione'          : forms.TextInput(attrs={'class':'form-control'}),
            'fg'                  : forms.TextInput(attrs={'class':'form-control'}),
            'mapp'                : forms.TextInput(attrs={'class':'form-control'}),
            'com_edil'            : forms.TextInput(attrs={'class':'form-control'}),
            'data_ce'             : forms.DateInput(),
            'tecnico'             : forms.TextInput(attrs={'class':'form-control'}),

        }


class DateInput(forms.DateInput):
    input_type = 'date'
    
        
class RichiedenteForm(forms.ModelForm):

    class Meta: 
        model = Pratica
        fields = ('richiedente',)


class MappaleForm(forms.ModelForm):
    
    class Meta:
        model = Pratica
        fields = ('fg','mapp',)

class TitoloForm(forms.ModelForm):
    
    class Meta:
        model = Pratica
        fields = ('atto',)


class IndirizzoForm(forms.ModelForm):

    civico = forms.CharField(
    widget=forms.TextInput(attrs={'readonly':'readonly'})
)

    class Meta:
        model = Pratica
        fields = ('ubicazione',)


class PraticaRegistration(forms.ModelForm):
    
    class Meta:
        model = Pratica
        fields = ('__all__')

    
        widgets = {

            'origine'             : forms.TextInput(attrs={'class':'form-control'}),
            'tipo'                : forms.TextInput(attrs={'class':'form-control'}),
            'istruttoria'         : forms.TextInput(attrs={'class':'form-control'}),
            'pos'                 : forms.TextInput(attrs={'class':'form-control'}),
            'data_prot_gen'       : forms.DateInput(),
            'prot_gen'            : forms.TextInput(attrs={'class':'form-control'}),
            'prot_urb'            : forms.TextInput(attrs={'class':'form-control'}),
            'num_atto'            : forms.TextInput(attrs={'class':'form-control'}),
            'data_atto'           : forms.DateInput(),
            'atto'                : forms.TextInput(attrs={'class':'form-control'}),
            'richiedente'         : forms.TextInput(attrs={'class':'form-control','autofocus': True}),
            'l_nasc'              : forms.TextInput(attrs={'class':'form-control'}),
            'd_nasc'              : forms.DateInput(),
            'citta'               : forms.TextInput(attrs={'class':'form-control'}),
            'residenza'           : forms.TextInput(attrs={'class':'form-control'}),
            'cod_fisc'            : forms.TextInput(attrs={'class':'form-control'}),
            'oggetto'             : forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':15}),
            'ubicazione'          : forms.TextInput(attrs={'class':'form-control'}),
            'fg'                  : forms.TextInput(attrs={'class':'form-control'}),
            'mapp'                : forms.TextInput(attrs={'class':'form-control'}),
            'com_edil'            : forms.TextInput(attrs={'class':'form-control'}),
            'data_ce'             : forms.DateInput(),
            'tecnico'             : forms.TextInput(attrs={'class':'form-control'}),

        }
        


class PraticaDetail(forms.ModelForm):
    class Meta:
        model = Pratica
        fields = ('__all__')


'''
    

class AllegatoAdd(forms.ModelForm):

    class Meta:
        model = Allegato
       
        fields = ('nome','doc',)

        widgets = {

            'nome'              : forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'doc'               : forms.FileInput(attrs={'class':'form-control'}),
            'pratica'           : forms.HiddenInput(),
            }


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

'''
