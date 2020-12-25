from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from Employee.models import Employee
from jobs.models import jobs
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from jobs.model_choices import *
from .models import Contact
# Create your views here.
def index(request):
    number = jobs.objects.all().count()
    latest = jobs.objects.filter(is_published=True).order_by('-published_date')[:4] # 0, 1, 2 ,3 object
    #   Listing.objects.order_by('-list_date')  ==> select * from Listing order by list_date Desc

    context = {

        'latest': latest,
        'Location': Location,
        'Category': Category,
        'count':number,

    }


    return render(request,'pages/index.html',context)

def Candidate(request):
    emp = Employee.objects.all()
    paginator = Paginator(emp, 4)
    page = request.GET.get('page', 1)
    try:
        paged_emp = paginator.get_page(page)
    except PageNotAnInteger:
        paged_emp = paginator.page(1)
    except EmptyPage:
        paged_emp = paginator.page(paginator.num_pages)
    context = {
        'emp': paged_emp,
    }
    return render(request,'pages/Candidate.html',context)

def Candidate_index (request,Employee_id):
    number=jobs.objects.all().count()
    context={
        'count':number,
    }
    Candidate_index_ = Employee.objects.get(id=Employee_id)
    return render (request, 'pages/Candidate_index.html', {'Candidate_index': Candidate_index_},context)

def contact(request):
    if request.method =='POST':
        dict_method=request.POST.copy()
        message=dict_method.get('message')
        name=dict_method.get('name')
        print(message)
        email=dict_method.get('email')
        subject=dict_method.get('subject')
        Contact.objects.create(message=message,
                               name=name,
                               email=email,
                               subject=subject,
                               report_date=True
                               )
        return HttpResponseRedirect(reverse('contact'))

    return render(request,'pages/contact.html')
def select_type(request):
    return render(request,'pages/select_type.html')