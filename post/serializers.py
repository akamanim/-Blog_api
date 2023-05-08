from rest_framework import serializers
from .models import Category, Tag, Post, Comment
from django.contrib.auth import get_user_model


User = get_user_model()

serializers.Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, title):
        if self.Meta.model.objects.filter(title=title).exists():
            raise serializers.ValidationError(
                'Пост с таким заголовком уже существует'
            )
        return title
    

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['comments'] = instance.comment.count()
        return representation

    


# class CommentSerializer(serializers.Serializer):
#     author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     body = serializers.CharField()
#     post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())


#     def create(self, validated_data):
#         return Comment.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.body = validated_data.get('body', instance.body)
#         ...
#         '''все поля'''
#         return instance
    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body', )

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'