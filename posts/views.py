from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, PostCreateSerializer, PostEditSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.authentication import TokenAuthentication


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreate(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_serializer_context(self):
        context = super(PostCreate, self).get_serializer_context()
        context.update({
            'author': self.request.user
        })
        return context


class PostEditView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostEditSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    authentication_classes = (TokenAuthentication,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
