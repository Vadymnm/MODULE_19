import sqlite3
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NameForm
from .models import *

def main(request):
    title = 'Главная страница'
    context = {
        'title': title,
        'main': "Главная",
        'shop': "Магазин",
        'bask': "Корзина", }
    return render(request, 'menu.html',context)


def games(request):
    # games_list = ["World of tanks", "Tetris", "Atomic Heart", "Cyberpunk", "PayDay" ]
    games_list = get_games()
    context = {
        'games_list': games_list,
         }
    return render(request, 'games.html', context)

# **** === Django === ********************************************************************
def get_games():
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM task1_game')
    lists = cursor.fetchall()
    games =[]
    for list in lists:
        x = [list[1],list[3],list[2]]
        print(x)
        games.append(x)
    print('games = ', games)
    return games

    connection.close


def get_users():
#    path = "D:\0-Мое обучение\UrbanUniversity\MODULE_19\Django"
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT name FROM task1_buyer')
    lists = cursor.fetchall()

    users =[]
    for list in lists:
        users.append(list[0])
    print('users = ', users)
    return users

    connection.close
#users = ['Vasya', 'Petya', 'Kolya']

# **** === Django === ********************************************************************

def reg_page_django(request):
    users = get_users()
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            passw = form.cleaned_data['passw']
            passw1 = form.cleaned_data['passw1']
            age = form.cleaned_data['age']

            info = {"name": name, "passw": passw, "age": age}
            print(info)
        # redirect to a new URL:
            if name in users:
                return HttpResponse("/!!! Пользователь уже существует !!!/")
            if passw != passw1:
                return HttpResponse("/!!! Пароли не совпадают !!!/")
            if int(age) < 18:
                return HttpResponse("/!!! Вы должны быть старше 18 !!!/")
            Buyer.objects.create(name=name, balance=0.0, age=age)
            return HttpResponse({"Приветствуем,", name})

        return render(request, 'reg_django.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, "reg_django.html", {"form": form})

#  ***** === HTML ==== **********************************************************

def reg_page_html(request):
    users = get_users()
    if request.method == "POST":
        name = request.POST.get('name')
        passw = request.POST.get('passw')
        passw1 = request.POST.get('passw1')
        age = request.POST.get('age')

        # print(f"name: {name}")
        # print(f"passw: {passw}")
        # print(f"passw1: {passw1}")
        # print(f"age: {age}")

        info = {"name": name, "passw": passw, "age": age}
        print(info)

        # redirect to a new URL:
        if name in users:
            return HttpResponse("/!!! Пользователь уже существует !!!/")
        if passw != passw1:
            return HttpResponse("/!!! Пароли не совпадают !!!/")
        if int(age) < 18:
            return HttpResponse("/!!! Вы должны быть старше 18 !!!/")
        Buyer.objects.create(name=name, balance=0.0, age=age)
        return HttpResponse({"Приветствуем,", name})

    return render(request, 'registration_page.html')
# ************************************************************************
