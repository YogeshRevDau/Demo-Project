from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
#from .models import CustomUser
#from .models import CustomUser
from django.contrib import messages
# Create your views here.
def RegisterView(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            #return HttpResponse('Login successfully')
            return redirect ('login')
    template_name='authapp/signup.html'
    context={'form':form}
    return render(request, template_name, context)


def loginView(request):
    print('inside login')
    if request.method == 'POST':
        print('USER IS POST')
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        print(un,pw)
        user=authenticate(request,username=un,password=pw)
        print('Auth',user)
        users=User.objects.all()
        print('***************************************************',users)
        print(user is  None)
        if user is not None:

            login(request,user)
            print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
            #return HttpResponse('Login successfully')
            return redirect('showdata')
        else:
            messages.error(request, 'Invalid username or password.')




    template_name='authapp/login.html'
    context={}
    return render(request, template_name, context)


def logoutView(request):

        logout(request)
        return redirect ('login')
from django.shortcuts import render

# Create your views here.
