from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordFrom 
from .models import Record

# Create your views here.
def home(request):
    records=Record.objects.all()

    # check to see if loggin in 

    if request.method=='POST':
        username=request.POST['username']  
        password=request.POST['password']
        # authenticate the user
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Login successful")
            return redirect('home')
        else:
            messages.success(request,"Login Failed pls try again")
            return redirect('home')
        
    else:    
        return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"Logout successful")
    return redirect('home')

def register_user(request):
    if request.method == 'POST': 
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate the user
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request," You hava Registration successful")
            return redirect('home')
    else:
        form=SignUpForm()    
        return render(request, 'register.html', {'form': form}, content_type=None, status=None, using=None)
    return render(request, 'register.html', {'form': form}, content_type=None, status=None, using=None)


def customer_record(request,pk):
    if request.user.is_authenticated:

        customer_record=Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record}, content_type=None, status=None, using=None)
    else:
         messages.success(request," You Must be Logged In To View That Page.. ")
         return redirect('home')
    
def delete_record(request,pk):
   if request.user.is_authenticated: 
       delete_it=Record.objects.get(id=pk)
       delete_it.delete() 
       messages.success(request,"Record Deleted Successfully...")
       return redirect('home')
   else:
       messages.success(request,"You must be login First")
       return redirect('home')
       
def add_record(request):
    form=AddRecordFrom(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Record Added Successfully")
                return redirect('home')    
        return render(request, 'add_record.html', {'form': form}, content_type=None, status=None, using=None)
    else:   
        messages.success(request,"You must be login First")
        return redirect('home')

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form =AddRecordFrom(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Updated Successfully")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form, 'current_record': current_record}, content_type=None, status=None, using=None)
    else:
        messages.success(request,"You must be login First")
        return redirect('home')    