from api.models import Article
from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer() 
    class Meta:
        model = Article 
        fields = ['title','author', 'date', 'text'] # remember you can use '__all__' instead of ['item','item'] to get all fields
        extra_kwargs = { 
                        'urls':{
                            'view_name': 'article_detail','lookup_field':'pk'
                            }}
