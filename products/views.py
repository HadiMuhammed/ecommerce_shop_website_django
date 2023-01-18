from django.shortcuts import render,redirect
from . import models
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
siteimages = models.siteimage.objects.all()
def index(request):
    products = models.product.objects.all()
    return render(request,"products.html",{'products':products,'logo':siteimages})

def register_user(request):
    form = CustomUserCreationForm()
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../login/')
    return render(request,"register.html",{'form':form,'logo':siteimages})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('../')
        else:
            messages.error(request,'Username or Password is incorrect!')    
    return render(request,"login.html")

def logout_user(request):
    logout(request)
    return redirect('login')  

def mycart(request):
    context = {}
    if request.user.is_authenticated:
        context["products"] = {models.cart.objects.filter(user=request.user)}
        context["logo"] = {models.siteimage.objects.all()}
    return render(request,"mycart.html",context)   

def add_to_cart(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            product_id = request.POST.get("id")
            total = request.POST.get("total")
            models.cart.objects.get_or_create(user=request.user,product=models.product.objects.get(pk=product_id),total=total,new_id=product_id)
        return redirect("home")
    else:
        messages.error(request,"Please login first !")
        return redirect("home")
def delete_from_cart(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            product_id = request.POST.get("id")
            instance = models.cart.objects.filter(new_id=product_id)
            instance.delete()
        return redirect("mycart")
    else:
        messages.error(request,"Please login first !")
        return redirect("mycart")    
            
