from django.urls import path, include
from .views import *
#	Si uso el app_name
#	ej: 
app_name = 'loan_app'

#api versioning
urlpatterns = [
	# Esta ruta genera GET POST PUT y DELETE
	path(
		'loan/',
		loan_list_view,
		name='loan'
	)
]