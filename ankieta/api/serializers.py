from rest_framework.serializers import ModelSerializer
from .models import Answers_Survey

class Asnwerserializer(ModelSerializer):
    class Meta:
        model=Answers_Survey
        fields='__all__' 
        
class Countserializer(ModelSerializer):
    class Meta:
        model=Answers_Survey
        fields=Answers_Survey.objects.count() 