from api.models import Post 
from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer() 
    class Meta:
        model = Post 
        fields = ['id', 'title','author', 'dateCreated', 'content'] # remember you can use '__all__' instead of ['item','item'] to get all fields
        extra_kwargs = { 
                        'urls':{
                            'view_name': 'article_detail','lookup_field':'pk'
                            }}
