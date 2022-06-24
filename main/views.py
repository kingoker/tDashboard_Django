from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db.models import Sum
from django.views.generic import UpdateView, DeleteView

from .models import *
from .forms import *


def main(request):
    order_to = OrderTo.objects.all()
    cotton = CottonPrice.objects.all()
    company_list = Profile.objects.order_by('-mark')[:5]
    yarn = Product.objects.filter(product_type_id=1)
    yarn_coast = yarn.aggregate(Sum('product_much'))
    material = Product.objects.filter(product_type_id=2)
    material_coast = material.aggregate(Sum('product_much'))
    tkan = Product.objects.filter(product_type_id=3)
    tkan_coast = tkan.aggregate(Sum('product_much'))

    data = {
        'yarn': yarn,
        'yarn_coast': yarn_coast,
        'material': material,
        'material_coast': material_coast,
        'tkan': tkan,
        'tkan_coast': tkan_coast,
        'cotton': cotton,
        'company_list': company_list.values(),
        'order_to': order_to,
    }

    return render(request, 'main/main.html', data)


def company(request, pk):
    cotton = CottonPrice.objects.all()
    order_to = OrderTo.objects.all()
    company_info = Profile.objects.filter(user_id=pk)

    data = {
        'company_info': company_info,
        'cotton': cotton,
        'order_to': order_to.values(),
    }

    return render(request, 'main/company.html', data)


def products(request, pk):
    cotton = CottonPrice.objects.all()
    order_to = OrderTo.objects.all()
    product_type = ProductType.objects.get(id=pk)
    product = Product.objects.filter(product_type_id=pk).order_by('-pk')

    data = {
        'product_type': product_type,
        'cotton': cotton,
        'order_to': order_to.values(),
        'product': product,
    }

    return render(request, 'main/products.html', data)


def order(request, pk):
    order_to = OrderTo.objects.all()
    order_type = OrderTo.objects.get(id=pk)
    cotton = CottonPrice.objects.all()
    company_list = Profile.objects.order_by('-mark')[:5]
    product = Product.objects.filter(order_to_id=pk)
    productType = ProductType.objects.all()

    yarn = product.filter(product_type_id=1)
    yarn_coast = yarn.aggregate(Sum('product_much'))
    material = product.filter(product_type_id=2)
    material_coast = material.aggregate(Sum('product_much'))
    tkan = product.filter(product_type_id=3)
    tkan_coast = tkan.aggregate(Sum('product_much'))

    data = {
        'yarn': yarn.values(),
        'yarn_coast': yarn_coast,
        'material': material,
        'material_coast': material_coast,
        'tkan': tkan.values(),
        'tkan_coast': tkan_coast,
        'product': product,
        'cotton': cotton,
        'company_list': company_list,
        'productType': productType,
        'order_to': order_to,
        'order_type': order_type,
    }
    return render(request, 'main/order.html', data)


def orderproducts(request, pk, id):
    cotton = CottonPrice.objects.all()
    order_to = OrderTo.objects.all()
    product = Product.objects.filter(order_to_id=pk).filter(product_type_id=id).order_by('-pk')

    data = {
        'product': product,
        'cotton': cotton,
        'order_to': order_to.values(),
    }

    return render(request, 'main/orderproducts.html', data)


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


class OrderEdit(UpdateView):
    model = Product
    template_name = 'main/order-edit.html'

    fields = ['order_to', 'product_type', 'product_number', 'product_mark', 'product_much', 'text']


class ProfileEdit(UpdateView):
    model = Profile
    template_name = 'main/profile-edit.html'
    order_to = OrderTo.objects.all()

    fields = ['title', 'log', 'adres', 'phone']


class OrderDelete(DeleteView):
    model = Product
    success_url = '/profile'
    template_name = 'main/order-delete.html'
    order_to = OrderTo.objects.all()


def registration(request):
    order_to = OrderTo.objects.all()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    data = {
        'order_to': order_to,
        'form': form,
    }
    return render(request, 'main/registration.html', data)


def user_login(request):
    order_to = OrderTo.objects.all()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()
    data = {
        'order_to': order_to,
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
