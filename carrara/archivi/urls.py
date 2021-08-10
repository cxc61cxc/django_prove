from django.urls import path, re_path
from . import views



urlpatterns = [
    
    path('', views.index, name='../../home/index'), # pagina principale
    path('mailer', views.index, name='../../mailer/index'), # pagina principale
   
        
    path('pratica_list_name/', views.pratica_list_name, name='pratica_list_name'), # listato pratiche per nominativo
    path('pratica_list_mapp/', views.pratica_list_mapp, name='pratica_list_mapp'), # listato pratiche per particella
    path('pratica_list_indirizzo/', views.pratica_list_indirizzo, name='pratica_list_indirizzo'), # listato pratiche per particella
    path('pratica_list_titolo/', views.pratica_list_titolo, name='pratica_list_titolo'),


    # stampe
    path('pdf_pratica/<int:pk>/', views.pdf_pratica, name='pdf_pratica'), 

    path('ricerca_nome/',views.name_pratica_list, name='ricerca_nome'), 
    path('ricerca_mapp/',views.mapp_pratica_list, name='ricerca_mapp'),
    path('ricerca_indirizzo/',views.indirizzo_pratica_list, name='ricerca_indirizzo'),
    path('ricerca_atto/',views.atto_pratica_list, name='ricerca_atto'),
    path('pratica_detail/<int:pk>/',views.pratica_detail, name='pratica_detail'),
    path('update_pratica/<int:pk>/',views.update_pratica, name="update_pratica"),
    path('pratica_add/',views.pratica_add, name="pratica_add"),


   



    path('posizione', views.posizione, name ='posizione'), #apre link su nominatim o su openstreetmap
    ]