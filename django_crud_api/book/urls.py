from django.urls import path, include
from .views import *
#	Si uso el app_name
#	ej: 
app_name = 'books_app'

#api versioning
urlpatterns = [
	# Esta ruta genera GET POST PUT y DELETE
	path(
		'new-book/',
		create_book,
		name='new_book'
	),
	path(
		'books/',
		book_list_view,
		name='books'
	),
]