from django.shortcuts import render, HttpResponse
from datetime import datetime 
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index_page(request):
    return render(request, 'index_page.html',)
def contact_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'contact_page.html')
    
def category_page(request):
    return render(request, 'category_page.html',)
def about_page(request):
    return render(request, 'about_page.html',)
