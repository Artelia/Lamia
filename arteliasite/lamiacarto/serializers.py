from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()
