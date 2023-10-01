from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = 'tasks_app'

router = routers.DefaultRouter()
router.register(r'tasks', TaskView, 'tasks')
#api versioning
urlpatterns = [
	path(
		'api/v1/',
		include(router.urls)
	)
	# Esta ruta genera GET POST PUT y DELETE
]