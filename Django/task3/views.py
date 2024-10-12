from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

number = 2


def start(request):
    title = 'Стартовая страница'
    context = {
        'title': title,
        'main': "Посты", }
    return render(request, 'start.html', context)


def index(request):
    global number
#    получаем все посты
    posts = Post.objects.all().order_by("-created_at")

    # создаем пагинатор
    # задаем число постов на странице - number
    if request.method == "POST":
        number = request.POST.get('number')
    print("number = ", number)

    paginator = Paginator(posts, number)  # n постов на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_obj = paginator.get_page(page_number)

    # передаем контекст в шаблон
    return render(request, 'index.html', {'page_obj': page_obj})
