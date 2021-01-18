from django.shortcuts import render
from .models import Book


def index(request):
	bookpage = Book.objects.all()
	return render(request, 'bookpage/book.html', {'bookpage': bookpage})  # Указываем какой шаблон мы будем показывать(после request)


class Books(object):
	@classmethod
	def as_view(cls):
		pass