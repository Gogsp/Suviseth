from SuvisethApp.models import Category, Customer, ServiceProvider
from SuvisethApp.forms import AdminForm, CategoryForm, ClientForm, ServiceProviderForm, UserForm
from django.shortcuts import redirect, render
from django.views.generic import View

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# # Create your views here.

def termsAndCondition(request):
    return render(request,'SuvisethApp/termsAndConditions.html')

def privacyAndPolicy(request):
     return render(request,'SuvisethApp/privacyAndPolicy.html')

def index(request):
    return render(request,'SuvisethApp/index.html')

def weddingServices(request):
    return render(request,'SuvisethApp/wedding_services.html')

@login_required
def findPartner(request):
    return render(request,'SuvisethApp/find_partner.html')

def signUp(request):
    return render(request,'SuvisethApp/registration.html')

def signIn(request):
    return render(request,'SuvisethApp/signin.html')

def clientSignup(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        client_form = ClientForm(data=request.POST)

        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            client = client_form.save(commit=False)
            client.user = user

            if 'profile_pic' in request.FILES:
                client.profile_pic = request.FILES['profile_pic']

            client.save()

            registered = True

        else:
            print(user_form.errors,client_form.errors)
    
    else:
        user_form = UserForm()
        client_form = ClientForm()

    return render(request,'SuvisethApp/client_signup.html',
                     {'user_form':user_form,
                    'client_form':client_form,
                    'registered':registered})

def sproviderSignup(request):
     
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        sprovider_form = ServiceProviderForm(data=request.POST)

        if user_form.is_valid() and sprovider_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            sprovider = sprovider_form.save(commit=False)
            sprovider.user = user

            if 'company_logo' in request.FILES:
                sprovider.company_logo = request.FILES['company_logo']

            sprovider.save()

            registered = True

        else:
            print(user_form.errors,sprovider_form.errors)
            print(user_form.errors,sprovider_form.errors)
    
    else:
        user_form = UserForm()
        sprovider_form = ServiceProviderForm()
    return render(request,'SuvisethApp/sprovider_signup.html',
                            {'user_form':user_form,
                        'sprovider_form':sprovider_form,
                        'registered':registered}) 

def adminSignup(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        admin_form = AdminForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            admin = admin_form.save(commit=False)
            admin.user = user

            if 'profile_pic' in request.FILES:
                admin.profile_pic = request.FILES['profile_pic']

            admin.save()

            registered = True
        else:
            print(user_form.errors,admin_form.errors)
    else:
        user_form = UserForm()
        admin_form = AdminForm()

    return render(request,'SuvisethApp/admin_signup.html',
                            {'user_form':user_form,
                            'admin_form':admin_form,
                            'registered':registered}) 

def clientSignin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('SuvisethApp:wedding_services'))
            else: 
                return redirect("Account not active")
        else:
            print('Some one is tried and failed')
            print("username : {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'SuvisethApp/client_signin.html')



def sproviderSignin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('SuvisethApp:wedding_services'))
            else: 
                return redirect("Account not active")
        else:
            print('Some one is tried and failed')
            print("username : {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'SuvisethApp/sprovider_signin.html')

def adminSignin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('SuvisethApp:wedding_services'))
            else: 
                return redirect("Account not active")
        else:
            print('Some one is tried and failed')
            print("username : {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'SuvisethApp/admin_signin.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('SuvisethApp:signin'))

@login_required
def categories(request):
    services = Category.objects.all()
    return render(request,'SuvisethApp/category/categories.html',
                            {'services':services})

@login_required
def add_category(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)

        if category_form.is_valid:
            category = category_form.save()
            

            if 'images' in request.FILES:
                category.images = request.FILES['images']
                category.save()
                return HttpResponseRedirect(reverse('SuvisethApp:categories'))
        
        else:
            print(category_form.errors)

    else:
        category_form = CategoryForm()

    return render(request,'SuvisethApp/category/add_category.html',
                        {'category_form':category_form})

@login_required
def edit_category(request,category_id):
    category = Category.objects.get(id=category_id)
    category_form = CategoryForm(instance=category)

    if request.method == "POST":
        category_form = CategoryForm(request.POST,instance=category)

        if category_form.is_valid:
            category = category_form.save()
            
            if 'images' in request.FILES:
                category.images = request.FILES['images']
                category.save()
                return HttpResponseRedirect(reverse('SuvisethApp:categories'))
        
        else:
            print(category_form.errors)

    return render(request,'SuvisethApp/category/edit_category.html',
                            {'category_form':category_form})

@login_required
def delete_category(request,category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('/categories')
    return render(request, 'SuvisethApp/category/delete_category.html',
                            {'category':category})

@login_required
def category(request,category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'SuvisethApp/category/category.html',
                            {'category':category})

@login_required
def service_providers(request):
    service_providers = ServiceProvider.objects.all()
    return render(request, 'SuvisethApp/admin_service_providers/all_service_providers.html',
                            {'service_providers':service_providers})

@login_required
def service_provider(request,sp_id):
    service_provider = ServiceProvider.objects.get(id=sp_id)
    return render(request, 'SuvisethApp/admin_service_providers/service_provider.html',
                            {'service_provider':service_provider})

@login_required
def edit_service_provider(request,sp_id):
    service_provider = ServiceProvider.objects.get(id=sp_id)
    s_provider_form = ServiceProviderForm(instance=service_provider)

    if request.method == "POST":
        s_provider_form = ServiceProviderForm(request.POST,instance=service_provider)

        if s_provider_form.is_valid:
            service_provider = s_provider_form.save()
            
            if 'company_logo' in request.FILES:
                service_provider.company_logo = request.FILES['company_logo']
                service_provider.save()
                return HttpResponseRedirect(reverse('SuvisethApp:all_service_providers'))
        
        else:
            print(s_provider_form.errors)
    return render(request, 'SuvisethApp/admin_service_providers/edit_service_provider.html',
                            {'sp_form':s_provider_form})

@login_required
def delete_service_provider(request,sp_id):
    sprovider = ServiceProvider.objects.get(id=sp_id)
    if request.method == 'POST':
        sprovider.delete()
        return redirect('/all_service_providers')
    return render(request, 'SuvisethApp/admin_service_providers/delete_service_provider.html',
                            {'sprovider':sprovider})

@login_required
def customers(request):
    customers = Customer.objects.all()
    return render(request,'SuvisethApp/admin_customers/all_customers.html',
                            {'customers':customers})

@login_required
def customer(request,c_id):
    customer = Customer.objects.get(id=c_id)
    return render(request,'SuvisethApp/admin_customers/customer.html',
                            {'customer':customer})

@login_required
def remove_customer(request,c_id):
    customer = Customer.objects.get(id=c_id)
    if request.method == 'POST':
        customer.user.delete()
        return redirect('/all_customers')
    return render(request,'SuvisethApp/admin_customers/remove_customer.html',
                            {'customer':customer})