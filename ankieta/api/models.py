from django.db import models

# Create your models here.
class Answers_Survey(models.Model):
    
    nr_zestawu=models.CharField(max_length=3,blank=True,null=True)
    plec=models.CharField(max_length=10,blank=True,null=True)
    wiek=models.CharField(max_length=2,blank=True,null=True)
    daltonizm=models.CharField(max_length=10,blank=True,null=True)
    
    Speech_1_colors=models.TextField(blank=True,null=True)
    Speech_1_colors_emotion=models.TextField(blank=True,null=True)
    Speech_2_colors=models.TextField(blank=True,null=True)
    Speech_2_colors_emotion=models.TextField(blank=True,null=True)
    Speech_3_colors=models.TextField(blank=True,null=True)
    Speech_3_colors_emotion=models.TextField(blank=True,null=True)
    Speech_4_colors=models.TextField(blank=True,null=True)
    Speech_4_colors_emotion=models.TextField(blank=True,null=True)
    Speech_5_colors=models.TextField(blank=True,null=True)
    Speech_5_colors_emotion=models.TextField(blank=True,null=True)
    Speech_6_colors=models.TextField(blank=True,null=True)
    Speech_6_colors_emotion=models.TextField(blank=True,null=True)
   
    
    Song_1_colors=models.TextField(blank=True,null=True)
    Song_1_colors_emotion=models.TextField(blank=True,null=True)
    Song_2_colors=models.TextField(blank=True,null=True)
    Song_2_colors_emotion=models.TextField(blank=True,null=True)
    Song_3_colors=models.TextField(blank=True,null=True)
    Song_3_colors_emotion=models.TextField(blank=True,null=True)
    Song_4_colors=models.TextField(blank=True,null=True)
    Song_4_colors_emotion=models.TextField(blank=True,null=True)
    Song_5_colors=models.TextField(blank=True,null=True)
    Song_5_colors_emotion=models.TextField(blank=True,null=True)
