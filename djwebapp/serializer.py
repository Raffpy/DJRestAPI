from django.db import models
from rest_framework import serializer
from models import Tutorial

class TutorialSerializer(serializer.ModelSerializer):

    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')