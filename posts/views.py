from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Post, CommentPost
from .serializers import *
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


class PostDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostEditSerializer
    authentication_classes = (TokenAuthentication,)


class CommentListView(generics.ListAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentSerializer


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        author = self.request.user
        post = Post.objects.get(pk=kwargs.get('pk'))
        if request.method == 'POST':
            serializer.is_valid(raise_exception=True)
            serializer.save(author=author, post=post)
            headers = self.get_success_headers(serializer.data)
            return Response({'Advertisement created successfully'},
                            status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'You do not have any permission to create comment here!!!'},
                            status=status.HTTP_400_BAD_REQUEST)


class CommentEditView(generics.UpdateAPIView):
    serializer_class = CommentEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CommentPost.objects.all()


class CommentDeleteView(generics.DestroyAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentEditSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    authentication_classes = (TokenAuthentication,)