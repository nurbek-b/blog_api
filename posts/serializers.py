from rest_framework import serializers
from .models import Post, CommentPost


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'image', 'body', 'created_at')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image', 'body')

    def create(self, validated_data):
        author = self.context.get('author')
        post = Post.objects.create(author=author, **validated_data)
        post.save()
        return post


class PostEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image', 'body')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        fields = ('id', 'author', 'post', 'body', 'created_at', 'updated_at')
        read_only_fields = ('author', 'post', 'body')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        fields = ('body',)


    # def create(self, validated_data):
    #     author = self.context.get('author')
    #     post = self.context.get('request')
    #     # print(post)
    #     comment = CommentPost.objects.create(author=author,
    #                                          post=post,
    #                                          **validated_data)
    #     comment.save()
    #     return comment


class CommentEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        fields = ('body',)
