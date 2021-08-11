from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'errormsg':'usernameまたはpasswordが一致しません'})

    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('login')
        