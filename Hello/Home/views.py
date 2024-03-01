from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.contrib import messages


def index(request):
    context={
        'variable':"this ia sent"
    }
    #return HttpResponse('hello my site')
    return render(request,'index.html',context)

def services(request):
    #return HttpResponse('services page')
    return render(request,'services.html')

def contact(request):
    #return HttpResponse('contact page')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact_instance = Contact(name=name, email=email, message=message)
        contact_instance.save()
        messages.success(request, "Conatct info sent.")
         
        
    return render(request,'contact.html')

def aboutus(request):
    #return HttpResponse('about page')
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')    
 
   

