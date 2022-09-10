from django.shortcuts import render


def login(request):
    return render(request, 'accounts/login.html', )


# def logout(request):
#     return render(request, 'account/logout.html', )


def signup(request):
    return render(request, 'accounts/signup.html', )
