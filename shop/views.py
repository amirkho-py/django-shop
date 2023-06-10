from django.shortcuts import render , get_object_or_404 , redirect
from .models import Slide , Product , Category , Contact
from .forms import ContactForm , RegisterForm , LoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required



def index(request):
    
    all_slides = Slide.objects.all()
    products = Product.objects.all()
    category = Category.objects.all()
    
    data = {
        'all_slides' : all_slides,
        'products' : products,
        'categories' : category
        
    }
    
    
    return render(request , 'shop/index.html',context=data)




def detail(request,product_id):
    product = get_object_or_404(Product , pk=product_id)
    data = {
        'product' : product
    }
    return render(request , 'shop/single.html',context=data) 





def contact(request):
    
    
    if request.method == "GET":
        data = {
        'form' : ContactForm
        }
        return render(request , 'shop/contact.html',context=data)
    
    else:
        form = ContactForm(request.POST)
        
        if form.is_valid():
            
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
    
            new_con = Contact(name=name,phone=phone,message=message)
            
            new_con.save()
            
            messages.success(request,message="پیام شما با موفقیت ارسال شد با شما تماس خواهیم گرفت")
            
            return redirect('shop:contact')
        
        


def register(request):
    
    if request.user.is_authenticated:
        return redirect("shop:index")
    
    if request.method == "GET":
        data = {
        'form' : RegisterForm
        }
        return render(request , 'shop/register.html',context=data)
    

    else:
        
         form = RegisterForm(request.POST)
         
         if form.is_valid():
             
             
             name = form.cleaned_data['name']
             lname = form.cleaned_data['lname']
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             
             user = User.objects.create_user(username=username,password=password,first_name=name,last_name=lname)
             user.save()
             
             messages.success(request,message=f"{name} عزیز ثبت نام شما موفقیت آمیز بود")
             
             
             return redirect('shop:index')
        
        
    
    
def login_page(request):
    
    if request.user.is_authenticated:
        return redirect("shop:index")
    
    if request.method == "GET":
        data = {
        'form' : LoginForm
        }
        return render(request , 'shop/login.html',context=data)
    
    else:
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request , user)
                messages.success(request,"ورود موفقیت آمیز. خوش آمدید")
                return redirect("shop:index")
            else:
                messages.warning(request,"نام کاربری یا گذرواژه صحیح نمیباشد")
                return redirect("shop:login")
                
                

def logout_view(request):
    logout(request)
    
    return redirect("shop:login")
    
               
                

@login_required(login_url="shop:login")
def dashboard(request):
    
    return HttpResponse("پنل کاربری")             
                
                

            
        
        
       
    
