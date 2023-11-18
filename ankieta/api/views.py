from django.shortcuts import render
import rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Asnwerserializer
from .serializers import Countserializer
from .models import Answers_Survey

@api_view(['GET'])
def get_people_number(request):
    global answer
    answer=Answers_Survey.objects.count()
    ans={"number":answer}
    #print(answer)
    return Response((answer % 184)+1)
@api_view(['POST'])
def submit_answers(request):
    data=request.data
    print(data['nr_zestawu'])
    answer2=Answers_Survey.objects.create(
        
        nr_zestawu=(answer % 184)+1,
        plec=data['plec'],
        wiek=data['wiek'],
        daltonizm=data['daltonizm'],
      Speech_1_colors=data['Speech_1_colors'],
      Speech_1_colors_emotion=data['Speech_1_colors_emotion'],
      Speech_2_colors=data['Speech_2_colors'],
      Speech_2_colors_emotion=data['Speech_2_colors_emotion'],
      Speech_3_colors=data['Speech_3_colors'],
      Speech_3_colors_emotion=data['Speech_3_colors_emotion'],
      Speech_4_colors=data['Speech_4_colors'],
      Speech_4_colors_emotion=data['Speech_4_colors_emotion'],
      Speech_5_colors=data['Speech_5_colors'],
      Speech_5_colors_emotion=data['Speech_5_colors_emotion'],
      Speech_6_colors=data['Speech_6_colors'],
      Speech_6_colors_emotion=data['Speech_5_colors_emotion'],
      Song_1_colors=data['Song_1_colors'],
      Song_1_colors_emotion=data['Song_1_colors_emotion'],
      Song_2_colors=data['Song_2_colors'],
      Song_2_colors_emotion=data['Song_2_colors_emotion'],
      Song_3_colors=data['Song_3_colors'],
      Song_3_colors_emotion=data['Song_3_colors_emotion'],
      Song_4_colors=data['Song_4_colors'],
      Song_4_colors_emotion=data['Song_4_colors_emotion'],
      Song_5_colors=data['Song_5_colors'],
      Song_5_colors_emotion=data['Song_5_colors_emotion'],
    )
    serializer=Asnwerserializer(answer2,many=False)
    return Response(serializer.data)
