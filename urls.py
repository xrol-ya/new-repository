from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	path('', views.index),
	url('books/<slug:title>', views.Books.as_view(), name='books-section')
]