from django import forms

class UserForm(forms.Form):
    fname  = forms.CharField(max_length=50)
    lname = forms.CharField(max_length=50)
    email = forms.EmailField()
    nphone = forms.CharField(max_length=10,min_length=10,required=True)
    fname.widget.attrs.update({'class':'input--style-5','type':"text",'name':"fname",'style':'width:100%;','placeholder':"First Name"})
    lname.widget.attrs.update({'class':'input--style-5','type':"text",'name':"lname",'style':'width:100%;','placeholder':"Lastname Name"})
    email.widget.attrs.update({'class': 'input--style-5','type':"email",'name':"email"})
    nphone.widget.attrs.update({'class': 'input--style-5','type':"text",'name':"nphone",'pattern':"[0-9]{1,}","title":"กรอกเบอร์มือถือให้ถูกต้อง","placeholder":"Please enter your PhoneNumber 0-9"})

class ChangpassForm(forms.Form):
    email = forms.EmailField(required=True)
    oldpassword = forms.CharField(max_length=50,required=True)
    newpassword = forms.CharField(max_length=50,required=True)
    email.widget.attrs.update({'class': 'input--style-5','type':"email",'name':"email",'style':'width:400px;'})
    oldpassword.widget.attrs.update({'class':'input--style-5','type':"text",'name':"oldpassword",'style':'width:300px;'})
    newpassword.widget.attrs.update({'class':'input--style-5','type':"text",'name':"newpassword",'style':'width:300px;'})