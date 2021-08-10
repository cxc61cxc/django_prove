from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label ="Nome",max_length=30, required=True)
    last_name = forms.CharField(label ="Cognome",max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    


         # this function will be used for the validation
    def clean(self):
 
        # data from the form is fetched using super function
        super(SignUpForm, self).clean()
         
        # extract the email and text field from the data
        email = self.cleaned_data.get('email')
        
 
        # conditions to be met for the email length
        status = "@comune.carrara.ms.it" in email
        if  status == False:
            self._errors['email'] = self.error_class([
                'Indirizzo email non accettato, contatta l\'amministrazione'])
        
        # return any errors if found
        return self.cleaned_data