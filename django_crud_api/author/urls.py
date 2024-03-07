from django.urls import path, include
from .views import *
#	Si uso el app_name
#	ej: 
app_name = 'author_app'

#api versioning
urlpatterns = [
	# Esta ruta genera GET POST PUT y DELETE
	path(
		'new-author/',
		create_author,
		name='new_author'
	),
	path(
		'authors/',
		author_list_view,
		name='authors'
	),

	path(
		'new-item/',
		create_item,
		name='new_item'
	),
	path(
		'items/',
		ItemListView.as_view(),
		name='items'
	),
	path(
		'list-items/',
		item_list_view,
		name='list_items'
	),
]