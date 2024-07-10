from django.contrib.auth.models import User
from django.contrib.auth import  login, authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import Post
from api.serializers import PostSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema

from api.forms import SignupForm


@swagger_auto_schema(method="get", responses={200: "OK"})
@api_view(["GET"])
def getRoutes(_):
    routes = [
        {
            "Endpoint": "/posts/",
            "method": "GET",
            "body": None,
            "description": "returns array of posts",
        },
        {
            "Endpoint": "/posts/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single article object based on its ID",
        },
        {
            "Endpoint": "/posts/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates a new article with data sent in post request",
        },
        {
            "Endpoint": "/posts/delete/id",
            "method": "DELETE",
            "body": "",
            "description": "deletes an article based on its ID",
        },
    ]
    return Response(routes)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, context={"request": request}, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getPost(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, context={"request": request}, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def subscribe(request):
    form = SignupForm(request.data)
    if form.is_valid():
        user = form.save()
        login(request, user)  # Automatically logs in the user after signup
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Subscription successful.",
            },
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response(
            {"Form is not valid": form.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
