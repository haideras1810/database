from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.parsers import FileUploadParser, MultiPartParser, JSONParser
from .models import Board, Comment, Link, News, Poll, Poll_Option, Image, Document
from django.http import FileResponse
from .serializers import (BoardSerializer, CommentSerializer, LinkSerializer,
                          NewsSerializer, PollSerializer,PollOptionSerializer, CommentSerializer, ImageSerializer,DocumentSerializer)


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class= BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):

        user = request.user
        boards = user.board_set.all()
        serializer = self.get_serializer(boards, many = True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.user
        board = Board(owner = request.user)
        serializer = self.get_serializer(board, data=request.data)
        serializer.is_valid(raise_exception = True)
        board = serializer.save()
        board = Board.objects.get(pk=board.id)
        board.members.add(user)
        serializer = self.get_serializer(board)
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        board = get_object_or_404(queryset, **kwargs)
        if board.owner_id == request.user.id:

            serializer = self.get_serializer(board, data=request.data)
            if serializer.is_valid(raise_exception = True):
                board = serializer.save()

            return Response(serializer.data)
        else:
            return Response('Not Authorized')

    def destroy(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        board = get_object_or_404(queryset, **kwargs)
        print("yolo")
        if board.owner_id == request.user.id:
            self.perform_destroy(board)
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response('Not Authorized')

    def join(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        board = get_object_or_404(queryset, pk=self.kwargs['pk'])
        board.members.add(request.user)
        board = self.get_serializer(board)
        return Response(board.data)


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class= LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, *args, **kwargs):
        links = Link.objects.filter(board_id = self.kwargs['board_id'])
        serializer = self.get_serializer(links, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        board_id = self.kwargs['board_id']
        board = get_object_or_404(Board, pk=board_id)
        link = Link(owner = request.user, board = board)
        link = self.get_serializer(link, data=request.data)
        if link.is_valid(raise_exception=True):
            link.save()
            return Response(link.data)

    def destroy(self,request,  *args, **kwargs):
        board_id = self.kwargs['board_id']
        board = get_object_or_404(Board, pk=board_id)
        link = self.get_object()
        if request.user.id == board.owner_id and request.user.id == link.owner_id:
            self.perform_destroy(link)
            return Response(status=status.HTTP_204_NO_CONTENT)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class= NewsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, *args, **kwargs):
        news = News.objects.filter(board_id = self.kwargs['board_id'])
        serializer = self.get_serializer(news, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        board_id = self.kwargs['board_id']
        board = get_object_or_404(Board, pk=board_id)
        news = News(owner = request.user, board = board)
        news = self.get_serializer(news, data=request.data)
        if news.is_valid(raise_exception=True):
            news.save()
            return Response(news.data)

    def destroy(self,request,  *args, **kwargs):
        board_id = self.kwargs['board_id']
        board = get_object_or_404(Board, pk=board_id)
        news = self.get_object()
        if request.user.id == board.owner_id and request.user.id == news.owner_id:
            self.perform_destroy(news)
            return Response(status=status.HTTP_204_NO_CONTENT)

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class= PollSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, *args, **kwargs):
        polls = Poll.objects.filter(board_id = self.kwargs['board_id'])
        serializer = self.get_serializer(polls, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        board_id = self.kwargs['board_id']
        board = get_object_or_404(Board, pk=board_id)
        poll = Poll(owner = request.user, board = board)
        poll = self.get_serializer(poll, data=request.data)
        if poll.is_valid(raise_exception=True):
            poll.save()
            return Response(poll.data)

    def destroy(self,request,  *args, **kwargs):
        board_id = self.kwargs['board_id']
        board = get_object_or_404(Board, pk=board_id)
        poll = self.get_object()
        if request.user.id == board.owner_id and request.user.id == poll.owner_id:
            self.perform_destroy(poll)
            return Response(status=status.HTTP_204_NO_CONTENT)

class PollOptionViewSet(viewsets.ModelViewSet):
    queryset = Poll_Option.objects.all()
    serializer_class= PollOptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, *args, **kwargs):
        poll_options = Poll.objects.filter(poll_id = self.kwargs['poll_id'])
        serializer = self.get_serializer(poll_options, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        poll_id = self.kwargs['poll_id']
        poll = get_object_or_404(Poll, pk=poll_id)
        poll_option = Poll_Option(poll = poll)
        poll_option = self.get_serializer(poll_option, data=request.data)
        if poll_option.is_valid(raise_exception=True):
            poll_option.save()
            return Response(poll_option.data)

    def destroy(self,request,  *args, **kwargs):
        poll_id = self.kwargs['poll_id']
        poll = get_object_or_404(Poll, pk=poll_id)
        poll_option = self.get_object()
        if request.user.id == poll.owner_id:
            self.perform_destroy(poll_option)
            return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class= CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, *args, **kwargs):
        comments = Poll.objects.filter(board_id = self.kwargs['news_id'])
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        news_id = self.kwargs['news_id']
        news = get_object_or_404(News, pk=news_id)
        comment = Comment(commenter = request.user, news = news)
        comment = self.get_serializer(comment, data=request.data)
        if comment.is_valid(raise_exception=True):
            comment.save()
            return Response(comment.data)

    def destroy(self,request,  *args, **kwargs):
        news_id = self.kwargs['news_id']
        news = get_object_or_404(News, pk=news_id)
        comment = self.get_object()
        if request.user.id == news.owner_id:
            self.perform_destroy(comment)
            return Response(status=status.HTTP_204_NO_CONTENT)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes =(MultiPartParser, JSONParser,)

    def list(self, *args, **kwargs):
        images = Image.objects.filter(board = self.kwargs['board_id'])
        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        owner = request.user
        board = Board.objects.get(pk=self.kwargs['board_id'])
        image = Image(owner = owner, board = board)
        image = self.get_serializer(image, request.data)
        if image.is_valid(raise_exception=True):
            image.save()
            return Response(image.data)

    def destroy(self,request,  *args, **kwargs):
        board_id = self.kwargs['board_id']
        image = self.get_object()
        if request.user.id == image.owner_id and image.board_id == board_id:
            self.perform_destroy(image)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('Not Authorized')

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes =(MultiPartParser, JSONParser,)

    def list(self, *args, **kwargs):
        docs = Document.objects.filter(board = self.kwargs['board_id'])
        serializer = self.get_serializer(docs, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        owner = request.user
        board = Board.objects.get(pk=self.kwargs['board_id'])
        doc = Document(owner = owner, board = board)
        doc = self.get_serializer(doc, request.data)
        if doc.is_valid(raise_exception=True):
            doc.save()
            return Response(doc.data)

    def destroy(self,request,  *args, **kwargs):
        board_id = self.kwargs['board_id']
        doc = self.get_object()
        if request.user.id == doc.owner_id and doc.board_id == board_id:
            self.perform_destroy(doc)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('Not Authorized')