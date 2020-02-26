from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
# when using "serializers.serializer" need to specify all the you have in your model
# no nee to specify all these fields when you use Modelserializer instead of Seializer
    title  = serializers.CharField(max_length = 100)
    author = serializers.CharField(max_length = 100)
    email  = serializers.EmailField(max_length = 100)
    date   = serializers.DateTimeField()    

    # for creation
    def create(self, validated_data):
        return Article.objects.create(validated_data)

    # to update & return the instance of the existing validated_data
    def update(self, instance, validated_data):
        instance.title  = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email  = validated_data.get('email', instance.email)
        instance.date   = validated_data.get('date', instance.date)
        # to save the instance
        instance.save()
        return instance

