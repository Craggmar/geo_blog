from rest_framework import serializers
from blogapp.models import Topic

class TopicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Topic
    fields = '__all__'
