from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']
        #verify user information
        if password == con_password:
            if User.objects.filter(username=user_name).exists():
                print('username already taken')
            elif User.objects.filter(email=email).exists():
                print('email already exists')
            else:
                user = User.objects.create_user(username=user_name, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
        else:
            print('password not matching ..')

        
        return redirect('/')
    else:
        return render(request, 'accounts/register.html')
    

