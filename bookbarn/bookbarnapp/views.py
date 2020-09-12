from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
#from .models import Profile
from .forms import BookCreateForm
from logregapp.models import *

def homepage(request):
    context = {
        'user_info': User.objects.get(id=request.session['user_id']),
        'all_books': Book.objects.all()
    }
    return render(request, 'homepage.html', context)

def account(request, id):
    context = {
        'user_info': User.objects.get(id=id),
        'profile': Profile.objects.all()
    }
    return render(request, 'account.html', context)

def edit(request):
    profile_model = Profile()
    _, photo = request.FILES.popitem()
    photo = photo[0]
    profile_model.photo = photo
    profile_model.save()
    return redirect('/bookbarn/homepage')

def favorited_books(request, id):
    context = {
        'user_info': User.objects.get(id=id)
    }
    return render(request, 'favorited.html', context)

def orders(request, id):
    context = {
        'user_info': User.objects.get(id=id)
    }
    return render(request, 'orders.html', context)

def requests(request, id):
    context = {
        'user_info': User.objects.get(id=id)
    }
    return render(request, 'requests.html', context)

def add_fave(request, id):
    faved_book = Book.objects.get(id=id)
    user_fave = User.objects.get(id=request.session['user_id'])
    faved_book.faves.add(user_fave)
    return redirect('/bookbarn/homepage')

def delete(request, id):
    Book.objects.get(id=id).delete()
    return redirect('/bookbarn/homepage')

#@login_required
def listing(request):
    if request.method == 'POST':
        form = BookCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.seller = User.objects.get(id=request.session['user_id'])
            new_item.save()
            print(new_item, '**')
            #messages.success(request, 'Book added successfully')
            return redirect('/bookbarn/homepage')
    else:
        form = BookCreateForm(data=request.GET)
    return render(request, 'listing.html', {'section': 'images', 'form': form})

def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug)
    return render(request, 'detail.html', {'section': 'images', 'image': book})