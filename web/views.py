from django.shortcuts import render, redirect
from .forms import LoginUserForm,CreateUserForm
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate 
from django.contrib.auth.decorators import login_required 
from .models import Record 
from django.contrib import messages

# - Home page
def home(request):
    return render(request, 'index.html')


# - Register User 
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect("my-login")
            

    context = {'form':form}

    return render(request, 'register.html',context=context)         



# - Login User
def my_login(request):

    form = LoginUserForm()

    if request.method == "POST":
        form = LoginUserForm(request,data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)

                
                return redirect("dashboard")
    context = {'form2':form}
    return render(request,'my-login.html',context=context)             


# - Logout User

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logged out successfully!")
    return redirect("my-login")




# - Dashboard 

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'dashboard.html', context=context)



def creator(request):
        return render(request,'creator.html')