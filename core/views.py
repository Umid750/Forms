from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    data = Product.objects.all()
    context = {
        'data':data
    }
    return render(request, 'index.html', context)

def add(request):
    form = ProductForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add.html', {'form':form})

def delete(request, id):
    delete_post = Product.objects.get(id = id)
    delete_post .delete()
    return redirect('home')

def edit(request, id):
    post = Product.objects.get(id = id)
    return render(request, 'update.html', {'post':post})
def editrecord(request, id):
    name = request.POST['name']
    company = request.POST['company']
    price = request.POST['price']
    category = request.POST['category']
    date = request.POST['date']
    image = request.POST['image']

    malumot = Product.objects.get(id = id)
    malumot.name = name
    malumot.company = company
    malumot.price = price
    malumot.category = category
    malumot.date = date
    malumot.image = image
    malumot.save()
    return redirect('home')
    
