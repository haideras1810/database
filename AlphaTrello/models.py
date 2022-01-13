from django.db import models
from django.contrib.auth.models import User
# Create your models here. 

class Board(models.Model):
    title = models.CharField(max_length= 100)
    members = models.ManyToManyField(User, through = 'Membership')
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name='owned_boards')

class News(models.Model):
    content = models.CharField(max_length=500)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Image(models.Model):
    src = models.FileField(upload_to='uploads')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Document(models.Model):
    src = models.FileField(upload_to='uploads')
    title = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Link(models.Model):
    src = models.CharField(max_length=280)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
class Poll(models.Model):
    poll_text = models.CharField(max_length=500)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

class Poll_Option(models.Model):
    option_text = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete= models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length = 500)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)

class Membership(models.Model):
    board = models.ForeignKey(Board, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)