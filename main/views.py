from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import CottonPrice, Product, Rating, OrderTo, ProductType
from .forms import ProductForm, UserRegisterForm, UserLoginForm, RatingForm


def main(request):
    order_to = OrderTo.objects.all()
    cotton = CottonPrice.objects.all()
    company_list = User.objects.all()
    productType = ProductType.objects.all()
    yarn_coast = Product.objects.filter(product_type_id=1)
    material_coast = Product.objects.filter(product_type_id=2)
    tran_coast = Product.objects.filter(product_type_id=3)
    data = {
        'material_coast': material_coast,
        'yarn_coast': yarn_coast,
        'productType': productType,
        'cotton': cotton,
        'company_list': company_list,
        'order_to': order_to,
    }

    return render(request, 'main/main.html', data)


def order(request, pk):
    order_to = OrderTo.objects.all()
    cotton = CottonPrice.objects.all()
    company_list = User.objects.all()
    product = Product.objects.filter(order_to_id=pk)

    data = {
        'product': product,
        'cotton': cotton,
        'company_list': company_list,
        'order_to': order_to,
    }
    return render(request, 'main/order.html', data)


@login_required
def profile(request):
    order_to = OrderTo.objects.all()
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
        'order_to': order_to,
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
    order_to = OrderTo.objects.all()
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
        'order_to': order_to,
        'rating_list': rating_list,
        'cotton': cotton,
        'form': form,
    }
    return render(request, 'main/rating.html', data)
