from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('login')

    else:
      return render(request,'login.html')
      messages.info(request,'Password or Username incorrect..!!')

def registr(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username Already Exist')
                messages.info(request,'Username Already Exist')
                return redirect('registr')
            elif User.objects.filter(email=email).exists():
                print('This emailid has another account')
                messages.info(request,'This emailid has another account')
                return redirect('registr')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('User Created')
                return render('login')
        else:
            messages.info(request,'Password not match')
            return redirect('registr')
        return redirect('/')
    else:
        return render(request,'registr.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

