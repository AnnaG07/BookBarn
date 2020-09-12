from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage),
    path('account/<int:id>', views.account),
    path('edit/<int:id>', views.edit),
    path('favorited_books/<int:id>', views.favorited_books),
    path('orders/<int:id>', views.orders),
    path('requests/<int:id>', views.requests),
    path('add_fave/<int:id>', views.add_fave),
    path('delete/<int:id>', views.delete),
    path('listing', views.listing),
    path('detail/<int:id>/<slug:slug>', views.book_detail)
]