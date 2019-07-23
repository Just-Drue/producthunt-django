from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})


@login_required(login_url='/accounts/signup')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] \
                and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            render(request, 'products/create.html', {'error': 'All fields are required!'})
    return render(request, 'products/create.html')


def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.html', {'product': product})


@login_required(login_url='/accounts/signup')
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
