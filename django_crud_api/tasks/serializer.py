from rest_framework import serializers
from .models import Task
class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model=Task
		#aqui paso los campos que quiero serializar a json de mi modelo
		fields=('id','title','description','done')