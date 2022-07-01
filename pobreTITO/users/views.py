import requests
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import User


def index(request):
    context = {"navBar": True}

    return render(request, "users/index.html", context)


def login_cidi(request):
    url = 'https://drt.sanfrancisco.gov.ar/webapi103/api/users'
    query_string = request.GET.get("querystring", "").replace(' ', '+')
    if query_string:
        json = {"QueryString": query_string, "User": "Muni103", "Password": "gJ4*mzrF!X!z"}
        r = requests.post(url, json=json)
        data = r.json()
        if data:
            cuil_cuim = data['Cuim']
            users = User.objects.filter(username=cuil_cuim)
            if users:
                login(request, users[0])
            else:
                full_name = data['Nombre']
                last_name, first_name = full_name.split(" ", 1)
                email = data['Mail']
                phone = data['Telefono']
                mobile = data['Celular']
                user, created = User.objects.get_or_create(username=cuil_cuim, email=email, cuil_cuim=cuil_cuim, phone=phone,
                                                           mobile=mobile, first_name=first_name, last_name=last_name)
                login(request, user)
            return redirect('new_claim')

        else:
            return redirect('home')

    else:
        return redirect('home')


@login_required
def logout_user(request):
    logout(request)

    return redirect("index")
