from django.shortcuts import render, redirect


def signup(request):
    buyer_email = request.POST['buyer_email']
    buyer_pass = request.POST['buyer_password']
    return redirect('buyers/signin.html')


def signin(request):
    pass


def change_password(request):
    pass


def paid_products(request):
    pass