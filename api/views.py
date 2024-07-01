from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from api.models import Article
from api.serializers import ArticleSerializer,UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    responses={200: 'OK'}
)

@api_view(['GET'])
def getRoutes(req):
    routes = [{
        'Endpoint' : '/articles/',
        'method' : 'GET',
        'body' : None,
        'description' : 'returns array of articles'

        },
              {
                  'Endpoint' : '/articles/id',
                  'method' : 'GET',
                  'body': None,
                  'description' : 'Returns a single article object based on its ID'

                  },
              {
   'Endpoint' : '/articles/create/',
                  'method' : 'POST',
                  'body': {'body': ""},
                  'description' : 'Creates a new article with data sent in post request'


                  },
{
   'Endpoint' : '/articles/delete/id',
                  'method' : 'DELETE',
                  'body': "",
                  'description' : 'deletes an article based on its ID'


                  },
              ]
    return Response(routes)

@api_view(['GET'])
def getArticles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles,context={'request': request},many=True)
    return Response(serializer.data)
 
@api_view(['GET'])
def getArticle(request, pk):
    articles = Article.objects.get(id=pk)
    serializer = ArticleSerializer(articles,context={'request': request},many=False)
    return Response(serializer.data)
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
