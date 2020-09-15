from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
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
    }
    return render(request, 'account.html', context)

def edit_account(request, id):
    if request.method == 'POST':
        edit_account = get_object_or_404(User, id=request.session['user_id'])
        edit_account.address = request.POST['address']
        edit_account.photo = request.FILES['photo']
        edit_account.save()
        print(edit_account)
        #return redirect('/bookbarn/account') #throws KeyError 'photo'
        return redirect('/bookbarn/homepage')

def detail(request, id):
    context = {
        'book': Book.objects.get(id=id)
    }
    return render(request, 'detail.html', context)

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
    return redirect('/bookbarn/homepage')

def remove_fave(request, id):
    faved_book = Book.objects.get(id=id)
    un_fave = User.objects.get(id=request.session['user_id'])
    faved_book.faves.remove(un_fave)
    return redirect('/bookbarn/homepage')
    #return redirect('/bookbarn/favorited_books')

def orders(request, id):
    context = {
        'user_info': User.objects.get(id=id)
    }
    return render(request, 'orders.html', context)

def requests(request, id):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user_info': User.objects.get(id=request.session['user_id']),
        'user_books': user.book_requestor.all(),
    }
    return render(request, 'requests.html', context)

def messenger(request, id):
    requests_by_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user_info': User.objects.get(id=request.session['user_id']),
        'book_request':Book.objects.get(id=id),
        'all_requests': requests_by_user.book_requestor.all(),
        'all_comments': Comment.objects.all(),
    }
    return render(request, 'messenger.html', context)

def post_comment(request, id):
    if request.method == 'POST':
        poster = User.objects.get(id=request.session['user_id'])
        requested = Requests.objects.get(id=id)
        Comment.objects.create(content=request.POST['content'], request=requested, poster=poster)
        return render(request, 'messenger.html')
        #return redirect('/bookbarn/messenger')

def make_request(request, id):
    context = {
        'user_info': User.objects.get(id=request.session['user_id']),
        'book': Book.objects.get(id=id),
    }
    return render(request, 'make_request.html', context)

def update_request(request, id):
    if request.method == 'POST':
        requestor = User.objects.get(id=request.session['user_id'])
        book = Book.objects.get(id=id)
        Requests.objects.create(content=request.POST['content'], book=book, requestor=requestor)
        return redirect('/bookbarn/homepage')

def delete(request, id):
    Book.objects.get(id=id).delete()
    return redirect('/bookbarn/homepage')

def listing(request):
    if request.method == 'POST':
        form = BookCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.seller = User.objects.get(id=request.session['user_id'])
            new_item.save()
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