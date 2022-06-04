from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import CottonPrice, Product, Rating
from .forms import ProductForm, UserRegisterForm, UserLoginForm, RatingForm


def sell(request):
    cotton = CottonPrice.objects.all()
    company_list = User.objects.all()
    data = {
        'cotton': cotton,
        'company_list': company_list,
    }
    return render(request, 'main/sell.html', data)


def buy(request):
    cotton = CottonPrice.objects.all()
    company_list = User.objects.all()
    data = {
        'cotton': cotton,
        'company_list': company_list,
    }
    return render(request, 'main/buy.html', data)


@login_required
def profile(request):
    cotton = CottonPrice.objects.all()
    buy = Product.objects.filter(author=request.user.pk, order_to='1')
    sell = Product.objects.filter(author=request.user.pk, order_to='2')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author_id = request.user.pk
            product.save()
            return redirect('profile')
    else:
        form = ProductForm()

    data = {
        'sell': sell,
        'buy': buy,
        'cotton': cotton,
        'form': form,
    }
    return render(request, 'main/profile.html', data)


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    data = {
        'form': form,
    }
    return render(request, 'main/registration.html', data)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()
    data = {
        'form': form,
    }
    return render(request, 'main/login.html', data)


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def rating(request):
    cotton = CottonPrice.objects.all()
    rating_list = Rating.objects.all()

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.author_id = request.user.pk
            rating.save()
            return redirect('rating')
    else:
        form = RatingForm()

    data = {
        'rating_list': rating_list,
        'cotton': cotton,
        'form': form,
    }
    return render(request, 'main/rating.html', data)
