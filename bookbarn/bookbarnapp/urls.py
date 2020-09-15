from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage),
    path('account/<int:id>', views.account),
    path('edit_account/<int:id>', views.edit_account),
    path('favorited_books/<int:id>', views.favorited_books),
    path('add_fave/<int:id>', views.add_fave),
    path('remove_fave/<int:id>', views.remove_fave),
    path('orders/<int:id>', views.orders),
    path('requests/<int:id>', views.requests),
    path('make_request/<int:id>', views.make_request),
    path('update_request/<int:id>', views.update_request),
    path('messenger/<int:id>', views.messenger),
    path('post_comment/<int:id>', views.post_comment),
    path('delete/<int:id>', views.delete),
    path('listing', views.listing),
    path('edit_listing/<int:id>', views.edit_listing),
    path('update_listing/<int:id>', views.update_listing),
    path('detail/<int:id>', views.detail),
]