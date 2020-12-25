from django.urls import path

from .import views


urlpatterns = [
    path('', views.index,name='index'),
    path('Candidate',views.Candidate,name='Candidate'),
    path('contact',views.contact,name='contact'),
    path('select_type',views.select_type,name='select_type'),
    path('<int:Employee_id>',views.Candidate_index,name='Candidate_index'),


]