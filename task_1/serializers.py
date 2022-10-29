from rest_framework import serializers
from .models import  MyInfo

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInfo
        fields = ['slackUsername', 'backend', 'age', 'bio']