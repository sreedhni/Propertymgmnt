from django import forms
from realestate.models import User,Property,Unit,Tenant,Lease
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1","password2","phone","address"]

class LoginForm(forms.Form):

    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class PropertyaddForm(forms.ModelForm):

    class Meta:
        model=Property
        fields="__all__"



class UnitAddForm(forms.ModelForm):
    class Meta:
        model=Unit
        exclude=("property",)




class TeanantCreateForm(forms.ModelForm):
    class Meta:
        model=Tenant
        fields="__all__"


class LeaseCreateForm(forms.ModelForm):
    class Meta:
        model=Lease
        exclude=("tenant","unit",)

        widgets={
            "agreement_end_date":forms.DateInput(attrs={"type":"date"})
         }

    