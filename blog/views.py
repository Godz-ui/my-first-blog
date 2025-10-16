from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect,render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, JsonResponse

from django.core.serializers.json import DjangoJSONEncoder


def index(request, name, age):
    bob = Person (name, age)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)


class Person:

    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age  # возраст человека


class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)







def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    # если возраст больше 17, то доступ разрешен
    if(age > 17):
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")





def user(request, name="Undefined", age =0):
    age = request.GET.get('age')
    name = request.GET.get('name')
    return HttpResponse(f"<h2>Имя: {name}  Возраст:{age}</h2>")

def contact(request):
    return HttpResponse("<h1>Контакты</h1>")



def products(request, id):
    return HttpResponse(f'Наш список товаров{id}')

def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")

def questions(request, id):
    return HttpResponse(f"Вопросы о товаре{id}")



def new(request):
    return HttpResponse('Новые товары')

def top(request):
    return HttpResponse('Наиболее популярные товары')

# //////////////// КУКИ ///////////////////

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response


# получение куки
def get(request):
    # получаем куки с ключом username
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")



# ////////////// HTML файлы ////////////////

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def info_list(request):  #Вшивание другого Html файла "contact_list"
    return render(request, 'blog/info_list.html')

def index_list(request):
    header = "Данные пользователя"
    langs = ['JavaScript', 'Python', 'Java']
    user = {"name": 'Arthur', "age": 38}
    address = ('Ибраева', 23, 12)

    data = {'header': header, 'langs':langs, 'user':user, 'address': address}
    return render(request, 'blog/index_list.html', context=data)
