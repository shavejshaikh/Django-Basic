from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100,default=None)
    author= serializers.CharField(max_length=100,default=None)
    email = serializers.EmailField(max_length=100,default=None)
    date  = serializers.DateTimeField()

    def create(self, validated_data):
        return Snippet.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title  = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email  = validated_data.get('email', instance.email)
        instance.date   = validated_data.get('date', instance.date)
        instance.save()
        return instance

class SnippetModelSerializer(serializers.Serializer):
    class Meta:
        model = Snippet   
        fields = ['id','title','author']