from rest_framework import serializers
from django.contrib.auth.models import User
from .models import News, Document, Image, Comment, Poll, Poll_Option, Link, Board
from accounts.serializers import UserSerializer


#

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields = ['id','content', 'owner_id', 'board_id', 'comment_set']
        read_only_fields= ['comment_set']
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields = ['id','title', 'src', 'owner_id', 'board_id']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields = ['id', 'src', 'owner_id', 'board_id']

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model=Poll
        fields = ['poll_text', 'poll_option_set']
        read_only_fields = ['poll_option_set']


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Poll_Option
        fields = ['id', 'option_text', 'poll_id']

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Link
        fields = ['id','src', 'board_id', 'owner_id']

class BoardSerializer(serializers.ModelSerializer):
    #owner = serializers.SerializerMethodField('get_owner')

    class Meta:
        model=Board
        fields = ['id', 'title', 'members', 'owner_id']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = ['id', 'content', 'news_id', 'commenter_id']