from django.shortcuts import render, redirect
from flask import redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url = "/login/")
 

# Create your views here.

def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        
        
        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description= recipe_description, 
            
            )
        
        return redirect('recipes')
    queryset = Recipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get("search"))
       
    
    
    
    context = {"recipes": queryset}
    
    return render(request, "recipes.html", context)

@login_required(login_url = "/login/")
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    context = {"recipe": queryset}
    
    if request.method == "POST":
        data = request.POST
        
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        
        if recipe_image:
            queryset.recipe_image = recipe_image
            
        queryset.save()
        return redirect("/recipes/")
    context = {'recipe': queryset}
        
    
    return render(request, "update_recipes.html", context)
   
    
    

@login_required(login_url = "/login/")
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/recipes/")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username"),
        password = request.POST.get("password"),
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, "invilid username")
            return redirect('/login/')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "invilid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipes/')
            
            
       
    return render(request, "login.html")



def logout_page(request):
    logout(request)
    return redirect("/login/")
    





def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name"),
        last_name = request.POST.get("last_name"),
        username = request.POST.get("username"),
        password = request.POST.get("password"),
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken.")
            return redirect('/register/')
            
        
        
        
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            
        )
        
        user.set_password('password')
        user.save()
        messages.info(request, "Account Created Successfully")
        
        return redirect('/register/')
        
        
    return render(request, "register.html")

def get_students(request):
    queryset = Student.objects.all()
    
    if request.Get.get('search'):
        queryset = queryset.filter()
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    
    print(page_obj)
    
    return render(request, "report/students.html", {"queryset": page_obj})

    
    
    


