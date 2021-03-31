from django.shortcuts import render, redirect
from django.conf import settings
from . import forms_master as fm
from . import models

# Create your views here.

def default_settings():
    context = {
        'site_title': settings.SITE_TITLE
    }
    return context

def defaultpage(request):
    print('lol')
    render(request,"base.html", {})

def index(request):
    haha = 'haha'
    return render(request, 'master.html', {'haha':haha})

def login(request):
    context = default_settings()
    return render(request, 'registration/login.html', context)

def add_products(request):
    curuser = request.user.id
    form = fm.form_add_product(request.POST)
    table = models.Products.objects.filter(user = curuser, unit__user=curuser)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    return render(request,"master/products.html",{'form':form, 'table':table})


def delete_product(request, id):
    models.Products.objects.get(id=id).delete()
    response = redirect('/tenants/master-product')
    return response


def edit_product(request, id):
    response = redirect('/tenants/master-product')
    return response
    
def add_unit(request):
    curuser = request.user.id
    form = fm.form_add_unit(request.POST)
    table = models.Units.objects.filter(user=curuser).only('name')
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    return render(request,"master/units.html",{'form':form, 'table':table})

def delete_unit(request, id):
    models.Units.objects.get(id=id).delete()
    response = redirect('/tenants/master-unit')
    return response

def edit_unit(request, id):
    response = redirect('/tenants/master-unit')
    return response
