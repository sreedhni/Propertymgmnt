from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse


from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator

from realestate.forms import UserRegistrationForm,LoginForm,PropertyaddForm,UnitAddForm,TeanantCreateForm,LeaseCreateForm
from realestate.models import User,Property,Unit,Lease,Tenant
from django.views.generic import View,CreateView,FormView,ListView,DetailView,TemplateView
from django.contrib.auth import authenticate,login,logout



def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session!!!")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper



def is_admin(fn):
    def wrapper(request,*args,**Kwargs):
        if request.user.is_superuser:
           return fn(request,*args,**Kwargs)
    return wrapper



def is_user(fn):
    def wrapper(request,*args,**Kwargs):
        if not request.user.is_superuser:
           return fn(request,*args,**Kwargs)
    return wrapper






ecs=[signin_required,is_user]


decs=[signin_required,is_admin]


class SignUpView(CreateView):

    template_name="register.html"
    form_class=UserRegistrationForm
    model=User
    success_url=reverse_lazy("signin")

    def form_valid(self, form):
         messages.success(self.request,"Account created")
         return super().form_valid(form)
    def form_invalid(self,form):
         messages.error(self.request,"failed to create")
         return super().form_invalid(form)
    
    
class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr.is_superuser:
                login(request,usr)
                messages.success(request,"login successfully")
                return redirect("index")
            elif not usr.is_superuser:
                return redirect("tenant-add")


            else:
                messages.error(request,"invalid creadential")
                return render(request,self.template_name,{"form":form})  
            
@method_decorator(decs,name="dispatch")

class IndexView(TemplateView):
    template_name="index.html"


@method_decorator(ecs,name="dispatch")

class TenantCreateView(CreateView):
     template_name="tenant_add.html"
     model=Tenant
     form_class=TeanantCreateForm
     success_url=reverse_lazy("tenant-add")

@method_decorator(ecs,name="dispatch")

class UPropertyListView(ListView):
    template_name="property.html"
    model=Property
    context_object_name="properties"

@method_decorator(ecs,name="dispatch")

class LeaseAddView(CreateView):
    form_class=LeaseCreateForm
    model=Lease
    template_name="lease_add.html"
    success_url=reverse_lazy("property-list")
    def form_valid(self, form):
       id=self.kwargs.get("pk")
       obj=Unit.objects.get(id=id)
       user=self.request.user
       tobj=Tenant.objects.get(name=user)
       form.instance.unit=obj
       form.instance.tenant=tobj
       return super().form_valid(form)
    

@method_decorator(decs,name="dispatch")

class PropertyCreateView(CreateView):
    template_name="property_add.html"
    form_class=PropertyaddForm
    model=Property
    success_url=reverse_lazy("property-all")

@method_decorator(decs,name="dispatch")

class PropertyListView(ListView):
    template_name="property_list.html"
    model=Property
    context_object_name="properties"

@method_decorator(decs,name="dispatch")

class PropertyDetailView(DetailView):
    template_name="property_detail.html"
    model=Property
    context_object_name="property"

@method_decorator(decs,name="dispatch")

class UnitAddView(CreateView):
    model=Unit
    form_class=UnitAddForm
    template_name="unit_add.html"
    success_url=reverse_lazy("property-all")

    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=Property.objects.get(id=id)
        form.instance.property=obj
        return super().form_valid(form)
    
@method_decorator(decs,name="dispatch")

class TenantView(ListView):
    model=Tenant
    template_name="tenant.html"
    context_object_name="tenant"
@method_decorator(decs,name="dispatch")

class LeaseDetailView(DetailView):
    template_name="lease_detail.html"
    model=Lease
    context_object_name="lease"

    

    
@method_decorator(decs,name="dispatch")

class LeaseView(ListView):
    model=Lease
    template_name="lease.html"
    context_object_name="lease"

@signin_required

def sign_out_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")  
    


    




    
    
    


