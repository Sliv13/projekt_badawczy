from django.shortcuts import render
import rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Asnwerserializer
from .models import Answers_Survey

@api_view(['POST'])
def submit_answers(request):
    data=request.data
    print(data['nr_zestawu'])
    answer=Answers_Survey.objects.create(
        
        nr_zestawu=data['nr_zestawu'],
        plec=data['plec'],
        wiek=data['wiek'],
        daltonizm=data['daltonizm'],
        Happiness_1=data['Happiness_1'],
        Happiness_2=data['Happiness_2'],
        Happiness_3=data['Happiness_3'],
        Happiness_4=data['Happiness_4'],
        Happiness_5=data['Happiness_5'],
        
        Anger_1=data['Anger_1'],
        Anger_2=data['Anger_2'],
        Anger_3=data['Anger_3'],
        Anger_4=data['Anger_4'],
        Anger_5=data['Anger_5'],
    
        Sadness_1=data['Sadness_1'],
        Sadness_2=data['Sadness_2'],
        Sadness_3=data['Sadness_3'],
        Sadness_4=data['Sadness_4'],
        Sadness_5=data['Sadness_5'],
        
        Surprise_1=data['Surprise_1'],
        Surprise_2=data['Surprise_2'],
        Surprise_3=data['Surprise_3'],
        Surprise_4=data['Surprise_4'],
        Surprise_5=data['Surprise_5'],
        
        Neutral_1=data['Neutral_1'],
        Neutral_2=data['Neutral_2'],
        Neutral_3=data['Neutral_3'],
        Neutral_4=data['Neutral_4'],
        Neutral_5=data['Neutral_5'],
        
        Disgust_1=data['Disgust_1'],
        Disgust_2=data['Disgust_2'],
        Disgust_3=data['Disgust_3'],
        Disgust_4=data['Disgust_4'],
        Disgust_5=data['Disgust_5'],
    )
    serializer=Asnwerserializer(answer,many=False)
    return Response(serializer.data)