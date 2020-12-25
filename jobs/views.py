from django.shortcuts import render
from .models import jobs,application
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from Employee.models import Employee
from .model_choices import Location,Category
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.contrib import messages,auth
# Create your views here.
def jobs_list(request):
    number = jobs.objects.all().count()
    dict_method=request.GET.copy()
    jobss = jobs.objects.filter(is_published=True)
    paginator=Paginator(jobss,4)
    page=request.GET.get('page',1)
    try:
        paged_jobs=paginator.get_page(page)
    except PageNotAnInteger:
        paged_jobs=paginator.page(1)
    except EmptyPage:
        paged_jobs=paginator.page(paginator.num_pages)
    context = {
        'jobss': paged_jobs,
        'count':number,
        'get_method':dict_method,

    }
    return render(request, 'jobs/jobs.html', context)
def job_index (request,jobs_id):

    job_index_ = jobs.objects.get(id=jobs_id)
    return render (request, 'jobs/job_index.html', {'job_index': job_index_})


def job_details(request):
    return render (request, 'jobs/job_details.html')
def search(request):
    dict_method = request.GET.copy()
    Keyword=dict_method.get('Keyword') or None
    jobss = jobs.objects.filter(is_published=True)
    paginator = Paginator(jobss, 4)
    page = request.GET.get('page', 1)
    try:
        paged_jobs = paginator.get_page(page)
    except PageNotAnInteger:
        paged_jobs = paginator.page(1)
    except EmptyPage:
        paged_jobs = paginator.page(paginator.num_pages)
    if 'Keyword' is not None:
        Keyword=dict_method.get('Keyword')
        jobss=jobss.filter(title__icontains=Keyword)

    if 'Location' in dict_method:
        Loc = dict_method.get('Location')
        jobss = jobss.filter(location__icontains=Loc)
    number=jobs.objects.all().count()

    if 'Category' in dict_method:
        Ctg = dict_method.get('Category')
        jobss = jobss.filter(category__iexact=Ctg)

    context = {
        'jobss': jobss,
        'Location': Location,
        'Category': Category,
        'get_method':dict_method,
        'count':number,
        'jobss':paged_jobs,

    }

    return render(request,'jobs/search.html',context)
def jop_post(request):
    if request.method=='POST':
        dict_method=request.POST.copy()
        name=dict_method.get('name')
        title=dict_method.get('title')
        position=dict_method.get('position')
        nature=dict_method.get('nature')
        salary=dict_method.get('salary')
        job_type=dict_method.get('job_type')
        location=dict_method.get('location')
        category=dict_method.get('category')
        logo=dict_method.get('logo')
        experiennce=dict_method.get('experience')
        qualification=dict_method.get('qualification')
        gender=dict_method.get('gender')
        vacency=dict_method.get('vacency')
        responsibilities=dict_method.get('responsibilities')
        benefit=dict_method.get('benefit')
        expired_date=dict_method.get('expired_date')
        date=dict_method.get('published_date')
        jobs.objects.create(Employee=name,
                            title=title,
                            position=position,
                            nature=nature,
                            salary=salary,
                            job_type=job_type,
                            location=location,
                            category=category,
                            logo=logo,
                            experience=experiennce,
                            qualification=qualification,
                            gender=gender,
                            responsibilities=responsibilities,
                            benefit=benefit,
                            is_published=False,
                            vacency=vacency,
                            published_date=date,
                            Employee_id=1,
                            expired_date=expired_date
                            )
        messages.success(request,'Job Posted Successfully')
        return HttpResponseRedirect(reverse('job_post'))
    return render(request,'jobs/job_post.html')

def job_applied(request):
    if request.method=='POST':

        dict_method=request.POST.copy()
        name=dict_method.get('name')
        email=dict_method.get('email')
        link=dict_method.get('link')
        cv=dict_method.get('cv')
        cover=dict_method.get('cover')
        application.objects.create(name=name,
                                   email=email,
                                   link=link,
                                   cv=cv,
                                   cover=cover
                                   )
        messages.success(request,'You have successfully applied!')
        return HttpResponseRedirect(reverse('index'))
    else:
        messages.error(request,'Something Went Wrong')
    return render(request,'pages/index.html')