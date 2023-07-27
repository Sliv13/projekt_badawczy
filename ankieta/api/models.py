from django.db import models

# Create your models here.
class Answers_Survey(models.Model):
    
    nr_zestawu=models.CharField(max_length=2,blank=True,null=True)
    plec=models.CharField(max_length=10,blank=True,null=True)
    wiek=models.CharField(max_length=2,blank=True,null=True)
    daltonizm=models.CharField(max_length=10,blank=True,null=True)
    
    Happiness_1=models.TextField(blank=True,null=True)
    Happiness_2=models.TextField(blank=True,null=True)
    Happiness_3=models.TextField(blank=True,null=True)
    Happiness_4=models.TextField(blank=True,null=True)
    Happiness_5=models.TextField(blank=True,null=True)
    
    Anger_1=models.TextField(blank=True,null=True)
    Anger_2=models.TextField(blank=True,null=True)
    Anger_3=models.TextField(blank=True,null=True)
    Anger_4=models.TextField(blank=True,null=True)
    Anger_5=models.TextField(blank=True,null=True)
    
    Sadness_1=models.TextField(blank=True,null=True)
    Sadness_2=models.TextField(blank=True,null=True)
    Sadness_3=models.TextField(blank=True,null=True)
    Sadness_4=models.TextField(blank=True,null=True)
    Sadness_5=models.TextField(blank=True,null=True)
    
    Surprise_1=models.TextField(blank=True,null=True)
    Surprise_2=models.TextField(blank=True,null=True)
    Surprise_3=models.TextField(blank=True,null=True)
    Surprise_4=models.TextField(blank=True,null=True)
    Surprise_5=models.TextField(blank=True,null=True)
    
    Neutral_1=models.TextField(blank=True,null=True)
    Neutral_2=models.TextField(blank=True,null=True)
    Neutral_3=models.TextField(blank=True,null=True)
    Neutral_4=models.TextField(blank=True,null=True)
    Neutral_5=models.TextField(blank=True,null=True)
    
    Disgust_1=models.TextField(blank=True,null=True)
    Disgust_2=models.TextField(blank=True,null=True)
    Disgust_3=models.TextField(blank=True,null=True)
    Disgust_4=models.TextField(blank=True,null=True)
    Disgust_5=models.TextField(blank=True,null=True)
    
    