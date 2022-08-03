from django.shortcuts import render
from django.db.models import Q
from .models import Categories, Productos


def home(request):

    categore = Categories.objects.all()[0:3]

    context = {"categore": categore}
    return render(request, 'base/index.html', context)


def contact(request):

    return render(request, 'base/contact.html')


def shop(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    prodact = Productos.objects.filter(
        Q(categories__name__icontains=q) |
        Q(title__icontains=q) |
        Q(brand__icontains=q)
    )

    categore = Categories.objects.all()

    context = {'prodact': prodact, "categores": categore}

    return render(request, 'base/shop.html', context)


def shopItem(request, pk):

    prodact = Productos.objects.get(id=pk)
    context = {'prodact': prodact}
    return render(request, 'base/shop-single.html', context)


def about(request):

    return render(request, 'base/about.html')


def userLogin(request):

    return render(request, 'base/reg/login.html')


def userReg(request):

    return render(request, 'base/reg/reg_login.html')
