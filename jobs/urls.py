from django.urls import path

from .import views

urlpatterns = [

    path('jobs/', views.jobs_list, name='jobs'),
    path('<int:jobs_id>',views.job_index,name='job_index'),
    path('job_details/',views.job_details,name='job_details'),
    path('search/',views.search,name='search'),
    path('post/',views.jop_post,name='job_post'),
    path('job_applied/',views.job_applied,name='job_applied')
]