from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required
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
        'user_info': User.objects.get(id=request.session['user_id']),
        #'profile': Profile.objects.get(id=id)
    }
    return render(request, 'account.html', context)

def edit_account(request, id):
    if request.method == 'POST':
        edit_account = get_object_or_404(User, id=request.session['user_id'])
        edit_account.address = request.POST['address']
        edit_account.photo = request.FILES['photo']
        edit_account.save()
        print(edit_account)
        return redirect('/bookbarn/homepage')


def favorited_books(request, id):
    context = {
        'fave_books': Book.objects.all(),
        'user': User.objects.get(id=id)
    }
    return render(request, 'favorited.html', context)

def add_fave(request, id):
    faved_book = Book.objects.get(id=id)
    user_fave = User.objects.get(id=request.session['user_id'])
    faved_book.faves.add(user_fave)
    print(user_fave, faved_book)
    return redirect('/bookbarn/homepage')

def remove_fave(request, id):
    faved_book = Book.objects.get(id=id)
    un_fave = User.objects.get(id=request.session['user_id'])
    faved_book.faves.remove(un_fave)
    print(un_fave, faved_book)
    return redirect('/bookbarn/homepage')
    #return redirect('/bookbarn/favorited_books')

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

def edit_listing(request, id):
    context = {
        'listing': Book.objects.get(id=id),
        'user_info': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'edit_listing.html', context)

def update_listing(request, id):
    if request.method == 'POST':
        listing = Book.objects.get(id=id)
        listing.url = request.POST['url']
        listing.title = request.POST['title']
        listing.desc = request.POST['desc']
        listing.price = request.POST['price']
        listing.listing_type = request.POST['listing_type']
        listing.save()
        print(listing)
        return redirect('/bookbarn/homepage')

def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug)
    return render(request, 'detail.html', {'section': 'images', 'image': book})