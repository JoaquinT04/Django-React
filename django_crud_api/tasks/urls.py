from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'tasks', TaskView, 'tasks')
#api versioning
urlpatterns = [
	# Esta ruta genera GET POST PUT y DELETE
	path(
		'api/v1/',
		include(router.urls)
	),
	path(
		'docs/',
		include_docs_urls(title="Tasks API")
		),
]