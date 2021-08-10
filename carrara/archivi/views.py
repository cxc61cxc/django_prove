from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Pratica
from .forms import RichiedenteForm,     MappaleForm, IndirizzoForm, PraticaRegistration, TitoloForm, PraticaAdd
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from xhtml2pdf import pisa
import csv  
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView



#pagina principale
def index(request):
    if request.user.is_authenticated:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is logged in :)")
                print(f"Username --> {request.user.username}")
    else:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is not logged in S: "+ ip_address + "-   " + messaggio)

    return render(request, 'archivi/index.html', {'ip_address': ip_address})


#listato tutte le pratiche per nominativo REGISTRATI
@login_required
def pratica_list_name(request):

    if request.method == "POST":
      
      form = RichiedenteForm(request.POST)
      if form.is_valid():
            richiedente = form.cleaned_data['richiedente']
            

            pratiche = Pratica.objects.filter(
                Q(richiedente__icontains=richiedente) |
                Q(oggetto__icontains=richiedente)).order_by('richiedente', '-data_prot_gen','fg','mapp')[:200]
            messaggio = 'Hai cercato : ' + richiedente
            if request.user.is_authenticated:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is logged in :)")
                print(f"Username --> {request.user.username}")
            else:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is not logged in : "+ ip_address + "-   " + messaggio)

            return render(request, 'archivi/pratica_list_name.html', {'pratiche':pratiche,'messaggio':messaggio,'ip_address':ip_address})
      else:
            return render(request, 'archivi/index.html', {})



# PDF
def pdf_pratica(request, *args, **kwargs):
    pk = kwargs.get('pk')
    pratica = get_object_or_404(Pratica,pk=pk)

    
    template_path = 'archivi/pdf_pratica.html'
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is not logged in : "+ ip_address)
    else:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is not logged in : "+ ip_address)
    context = {'pratica': pratica, 'ip_address': ip_address}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=richiesta_accesso_atti.pdf'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response





#lista tutte le pratiche per particella

def pratica_list_mapp(request):

    if request.method == "GET":
        particella = MappaleForm(request.GET)
        if particella.is_valid():
            fg = request.GET.get('fg',None)
            mapp = request.GET.get('mapp',None)
            if request.user.is_authenticated:
                pratiche = Pratica.objects.filter(
                Q(fg__icontains=fg) & Q(mapp__icontains=mapp)). \
                order_by('richiedente','origine','-fg','mapp')[:200]
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is logged in :)")
                print(f"Username --> {request.user.username}")
            else:
                # esclude dalla ricerca gli abusi edilizi
                pratiche = Pratica.objects.filter(
                Q(fg__icontains=fg) & Q(mapp__icontains=mapp))
                pratiche = pratiche.exclude(origine__startswith='abu').order_by('richiedente','origine','-fg','mapp')[:200]
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is not logged in : "+ ip_address)

            #pratiche = Pratica.objects.filter(
             #   Q(fg__icontains=fg) & Q(mapp__icontains=mapp)). \
              #  order_by('richiedente','origine','-fg','mapp')[:200]
            messaggio = 'Hai cercato : fg ' + fg +' mapp ' +mapp + ' (verifica nell\'elenco!)'
            return render(request, 'archivi/pratica_list_name.html', {'pratiche':pratiche, 'messaggio': messaggio, 'ip_address':ip_address})
        
        else:

            return render(request, 'archivi/index.html', {})




#lista tutte le pratiche per titolo

def pratica_list_titolo(request):

    if request.method == "POST":
        form = TitoloForm(request.POST)
        if form.is_valid():
            atto = form.cleaned_data['atto']
            pratiche = Pratica.objects.filter(
                
                Q(atto__icontains=atto) | 
                Q(num_atto__icontains=atto) |
                Q(istruttoria__icontains=atto) )
            
            if request.user.is_authenticated:
                pratiche=pratiche.order_by('richiedente','-data_prot_gen','-fg','mapp')[:200]
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is logged in :)")
                print(f"Username --> {request.user.username}")
            else:
                # esclude dalla ricerca gli abusi edilizi
                pratiche=pratiche.exclude(origine__startswith='abu').order_by('richiedente','-data_prot_gen','-fg','mapp')[:200]
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is not logged in : "+ ip_address)

        
            messaggio = 'Hai cercato : atto ' + atto + ' (verifica nell\'elenco!)'
            return render(request, 'archivi/pratica_list_name.html', {'pratiche':pratiche, 'messaggio': messaggio,'ip_address':ip_address})
        
        else:

            return render(request, 'archivi/index.html', {})

def atto_pratica_list(request):
    form = TitoloForm()
    if request.user.is_authenticated:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is not logged in : "+ ip_address)

    return render(request, 'archivi/ricerca_atto.html', {'form': form})




#listato tutte le pratiche per ubicazione


def pratica_list_indirizzo(request):
    if request.method == "POST":
      
        form = IndirizzoForm(request.POST)
        if form.is_valid():

            ubicazione = form.cleaned_data['ubicazione']
            civico = request.POST.get('civico',None)
            if civico != None:
                cerca_via = Pratica.objects.filter(
                Q(ubicazione__icontains=ubicazione))

                # cerco il civico tra le strade trovate sopra
                pratiche = cerca_via.filter(
                    Q(ubicazione__icontains=civico))
            else:
               pratiche = Pratica.objects.filter(
                Q(ubicazione__icontains=ubicazione)).order_by(
                'fg','mapp','richiedente','-data_prot_gen')[:200]

            # dice chi o l'ip
            if request.user.is_authenticated:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is logged in :)")
                print(f"Username --> {request.user.username}")
            else:
                # esclude dalla ricerca gli abusi edilizi
                pratiche = pratiche.exclude(origine__startswith='abu').order_by(
                    'fg','mapp','richiedente','-data_prot_gen')[:200]
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is not logged in : "+ ip_address )
            
            

            messaggio = 'Hai cercato ' + ubicazione + ' ' + civico
            return render(request, 'archivi/pratica_list_name.html', {'pratiche':pratiche, 'messaggio':messaggio, 'ip_address':ip_address})
    else:
            messaggio = ' qualcosa non funziona!'
            return render(request, 'archivi/index.html', {'messaggio':messaggio})

'''
           # paginazione
           page = request.GET.get('page', 1)

           paginator = Paginator(pratiche, 10)
           try:
               pratiche = paginator.page(page)
           except PageNotAnInteger:
               pratiche = paginator.page(1)
           except EmptyPage:
               pratiche = paginator.page(paginator.num_pages)
'''




def indirizzo_pratica_list(request):
    form = IndirizzoForm()
    if request.user.is_authenticated:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is not logged in : "+ ip_address)
    return render(request, 'archivi/ricerca_indirizzo.html', {'form': form})



@login_required

def name_pratica_list(request):
    form = RichiedenteForm()
    if request.user.is_authenticated:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is not logged in :"+ ip_address)
    return render(request, 'archivi/ricerca_nome.html', {'form': form, 'ip_address':ip_address})




def mapp_pratica_list(request):
    form = MappaleForm()
    if request.user.is_authenticated:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is not logged in :"+ ip_address)
    return render(request, 'archivi/ricerca_mapp.html', {'form': form})



def pratica_detail(request, pk):
    pratica = get_object_or_404(Pratica, pk=pk)
    if request.user.is_authenticated:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is not logged in :"+ ip_address)
    return render(request, 'archivi/pratica_detail.html', {'pratica': pratica, 'pk': pk})





def posizione(request, loc):
    posizione = get_object_or_404(Pratica, loc=loc)
    if request.user.is_authenticated:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        print("User is not logged in :"+ ip_address)
    posizione = "http://openstreetmap.org/search?query=Carrara"+posizione.loc
    
    return render(request, 'archivi/posizione.html', {'posizione': posizione})
    #return redirect("posizione")




#edit and update functionup
@login_required

@user_passes_test(lambda u: u.groups.filter(name='editor').count() == 1, login_url='home')

def update_pratica(request,pk):
    if request.method == 'POST':

        pi = Pratica.objects.get(pk=pk)
        form = PraticaRegistration(request.POST, instance=pi)

        if form.is_valid():
            if request.user.is_authenticated:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is logged in :)")
                print(f"Username --> {request.user.username}")
            else:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is not logged in :"+ ip_address)
            form.save()
            messaggio ='il record è stato aggiornato!'
            salvato = 'yes'

            return render(request, 'archivi/update_pratica.html', { 'form':form, 'messaggio':messaggio , 'salvato':salvato})
    else:
       
        pi = Pratica.objects.get(pk=pk)
        form = PraticaRegistration(instance=pi)
    return render(request,'archivi/update_pratica.html', {'form':form})    



@login_required
@user_passes_test(lambda u: u.groups.filter(name='editor').count() == 1, login_url='home')


def pratica_add(request):
    submitted = False
    if request.method == "POST":
        form = PraticaAdd(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_authenticated:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is logged in :)")
                print(f"Username --> {request.user.username}")
            else:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is not logged in :"+ ip_address)
            return HttpResponseRedirect('?submitted=True')
    else:
        form = PraticaAdd
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'archivi/pratica_add.html',{'form':form,'submitted':submitted})



####################################################################################
#
#                       Allegato
#####################################################################################



'''
def allegato_add(request,pk=None):
    submitted=False
    print(pk)
    if request.method == "POST":
            #print(str(pk)+' il get passa!')
            form = AllegatoAdd(request.POST,  request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['doc'])
                return HttpResponseRedirect('/success/url/')
            print(str(pk)+' il POST  passa e pure il form!')

    if request.method == "GET":
        #print(str(pk)+' il get passa!')
        form = AllegatoAdd(request.GET)
        print(str(pk)+' il get passa e pure il form!')

        if form.is_valid():
            print(str(pk)+' ... il form è valido')
            submitted=True

            form.save()
            return render(request,'archivi/success.html/',{'form':form})
    else:
        pk=pk
        print('l\'id della pratica '+ pk)
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'archivi/allegato_add.html/',{'pratica':pk, 'submitted':submitted})



# Create your views here.
def contact(request):
  if (request.method == 'POST'):
    name = request.POST.get('name')
    email = request.POST.get('email')
    desc = request.POST.get('desc')
    contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
    contact.save()
  return render(request, 'archivi/contact_form.html')

'''