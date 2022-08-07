from django.shortcuts import render,redirect,HttpResponse
import requests
from datetime import date
from django.core.paginator import Paginator,EmptyPage
import random
from .models import Content
from django.contrib import messages

apis_list = ["837f40ad0dfb47e5b73cab4b3375553a","cffb758a2a4e4ab5b6e2bea10b383593"]

def home(request):
    api = random.choice(apis_list)
    date_today = date.today()
    url = f'https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey={api}'


    
    category = ''
    if request.GET.get('category') :
        category = request.GET.get('category')
        url = f'https://newsapi.org/v2/top-headlines?category={category}&language=ar&apiKey={api}'


    if request.GET.get('country') :
        country = request.GET.get('country')
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api}'
        
    

    response = requests.get(url)
    result = response.json()
    # pagenation 
    p = Paginator(result['articles'],8)   
    page_number = request.GET.get('page',1) 
    
    page = p.page(page_number)


    context = {"result":page,
               "date_today":date_today}
    return render(request,'home.html',context)
 



def about(request):
    return render(request,'about.html')
    
def contect(request):
    if request.method == 'POST':
        Contect = Content()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        Contect.name=name
        Contect.email=email
        Contect.subject=subject
        Contect.save()
        return redirect('home')
    return render(request,'contact.html')
    
    
    
