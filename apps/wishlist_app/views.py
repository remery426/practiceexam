from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Product
from django.contrib import messages
# Create your views here.
def index(request):
    current_user = User.objects.get(username=request.session["thisuser"])

    context = {
        "current_user" : current_user,
        "all_products" : Product.objects.all(),
        "wishlist"     : current_user.wishlist
        }
    if request.session['thisuser'] == '':
        return redirect('/')

    return render(request,'wishlist_app/index.html', context)
def create_page(request):

    return render(request,'wishlist_app/create_page.html')
def create(request):
    response = Product.objects.create_product(request.POST, request.session['thisuser'])
    user_3 = User.objects.get(username=request.session['thisuser'])
    if not response['status']:
        for error in response['error']:
            messages.error(request, error)

        return redirect('wishlist_app/create_page')
    print response['item']
    return redirect('wishlist_app/dashboard')
def delete(request,id):
    current_item = Product.objects.get(id=id)
    current_item= Product.objects.get(id=id).delete()
    return redirect('wishlist_app/dashboard')
def add(request,id):
    this_user = User.objects.get(username = request.session['thisuser'])
    item = Product.objects.get(id=id)
    item.wishlist.add(this_user)
    return redirect('wishlist_app/dashboard')
def remove(request,id):
    this_user = User.objects.get(username = request.session['thisuser'])
    item = Product.objects.get(id=id)
    item.wishlist.remove(this_user)
    return redirect('wishlist_app/dashboard')
def logout(request):
    request.session['thisuser'] = ''
    return redirect('/')
def product_page(request,id):
    all_users = User.objects.all()
    product= Product.objects.filter(id=id)
    all_users1 = []
    all_users2 = []

    context = {
        "item" : product,
        "wishlist" : all_users2

}
    return render(request,'wishlist_app/product_page.html', context)
