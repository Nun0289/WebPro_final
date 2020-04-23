from django import forms

class UserForm(forms.forms):
    fname  = forms.CharField(max_length=50)
    lname = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50,required=True)
    email = forms.EmailField()
    nphone = forms.CharField(max_length=10,min_length=10,required=True)