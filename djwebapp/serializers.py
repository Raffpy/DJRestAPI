from django.db import models

from rest_framework import serializers
from djwebapp.models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')