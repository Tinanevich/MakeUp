from django.shortcuts import render, redirect
from .models import Customer, Comments
from .forms import CustomerForm, CommentsForm
from django.http import HttpResponseRedirect


def home(request):
    error = ''
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/price')
        else:
            error = 'Data is not correct!'
    form = CustomerForm()
    dict = {
        'form': form,
        'error': error
    }
    return render(request, 'index.html', dict)


def price(request):
    return render(request, 'price.html')

def comments(request):
    error = ''
    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = CommentsForm()
    text = Comments.objects.order_by('-id')
    dict = {
        'form': form,
        'text': text,
        'error': error,
    }
    return render(request, 'recorded.html', dict)