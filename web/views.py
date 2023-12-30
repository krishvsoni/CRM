from django.shortcuts import render, redirect
from .forms import LoginUserForm, CreateUserForm, CreateRecordForm , UpdateRecordForm
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate 
from django.contrib.auth.decorators import login_required 
from .models import Record 
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect



# - Home page

@csrf_protect
def home(request):
    return render(request, 'index.html')


# - Register User
#  
@csrf_protect
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect("my-login")
            

    context = {'form':form}

    return render(request, 'register.html',context=context)         



# - Login User
@csrf_protect

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
    messages.success(request,"Login Successfully")
    return render(request,'my-login.html',context=context)             


# - Logout User
@csrf_protect

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logged out successfully!")
    return redirect("my-login")




# - Dashboard 
@csrf_protect

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'dashboard.html', context=context)


# - Create Record
@csrf_protect

@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()
    
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("dashboard")
        
    context = {'form': form}

    messages.success(request, "Record created successfully!")
    return render(request, 'create-record.html',context=context)    


# - Update Record
@csrf_protect

@login_required(login_url = 'mylogin')
def update_record(request,pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request,'update-record.html',context=context)


 # - Read / View a singular record
@csrf_protect

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'view-record.html', context=context)



# - Delete a singular record

@csrf_protect

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")


# - Developer 

def creator(request):
        return render(request,'creator.html')
