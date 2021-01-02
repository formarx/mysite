from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error_msg': 'Username has already been taken.'})
            except User.DoesNotExist:
                try:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                except Exception as e:
                    print(e)
                auth.login(request, user)
                return redirect('home')
            except Exception as e:
                print("EEEE")
                print(e)
                return render(request, 'signup.html', {'error': str(e)})
        else:
            print("AAAAA")
            return render(request, 'signup.html')
    
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            render(request, 'login.html', {'error_msg': 'Username or password is not correct.'})
    else:
        return render(request, 'login.html')
