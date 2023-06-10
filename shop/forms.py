from django import forms


class ContactForm(forms.Form):
    
    name = forms.CharField(max_length=264,label="نام:",required=True,widget=forms.TextInput(attrs={'class':"form-control col-3"}))
    phone = forms.CharField(max_length=264,label="شماره تلفن:",required=True,widget=forms.TextInput(attrs={'class':"form-control col-3"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control col-3"}),label="پیام شما:",)
    
    
    


class RegisterForm(forms.Form):
     name = forms.CharField(max_length=264,label="نام:",required=True,widget=forms.TextInput(attrs={'class':"form-control col-3"}))
     lname = forms.CharField(max_length=264,label="نام خانوادگی:",required=True,widget=forms.TextInput(attrs={'class':"form-control col-3"}))
     username = forms.CharField(max_length=264,label="نام کاربری:",required=True,widget=forms.TextInput(attrs={'class':"form-control col-3"}))
     password = forms.CharField(max_length=264,label="گذرواژه:",required=True,widget=forms.PasswordInput(attrs={'class':"form-control col-3"}))
    
    
    
class LoginForm(forms.Form):
     username = forms.CharField(max_length=264,label="نام کاربری:",required=True,widget=forms.TextInput(attrs={'class':"form-control col-3"}))
     password = forms.CharField(max_length=264,label="گذرواژه:",required=True,widget=forms.PasswordInput(attrs={'class':"form-control col-3"}))
    