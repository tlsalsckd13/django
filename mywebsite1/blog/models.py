from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from users.models import User
# Create your models here.
# 글의 분류(일상 유머 정보)

class Category(models.Model):
    name = models.CharField(max_length=50, help_text="음악 장르를 입력하세요")

    def __str__(self):
        return self.name

# 블로그 글(제목, 작성일, 대표 이미지, 내용, 분류)
#class Post(models.Model):
#    title = models.CharField(max_length=200)
#    title_image = models.ImageField(blank = True)
#    content = models.TextField()
#    createDate = models.DateTimeField(auto_now_add = True)
#    updateDate = models.DateTimeField(auto_now_add=True)
#    #하나의 글을 여러가지의 분류에 해당될 수 있다.(ex: 정보,유머 등) 하나의 분류에는 여러가지 글이 포함될 수 있음 (정보 카테고리에 글 10개)
#    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요")

#    def __str__(self):
#        return self.title

class Music(models.Model):
    music_no = models.AutoField(primary_key=True)
    music_name = models.CharField(max_length=20)
    music_artist = models.ForeignKey("Artist", related_name="artist", on_delete=models.CASCADE)
    music_composer = models.CharField(max_length = 15)
    music_lyricsist = models.CharField(max_length = 15)
    music_lyrics = models.TextField()
    music_file = models.FileField(default='')

    def __str__(self):
        return self.music_name

# class Album(models.Model):
#    album_name = models.CharField(max_length=20)
#   album_image = models.ImageField(blank = True)
#   artist_name = models.ForeignKey("Artist", on_delete=models.CASCADE)

#    def __str__(self):
#        return self.album_name

class Artist(models.Model):
    artist_no = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=15)
    artist_category = models.ManyToManyField(Category, help_text="음악 장르를 설정하세요")

    def __str__(self):
        return self.artist_name

class Album(models.Model):
    album_no = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=15, default='')
    album_artist_no = models.ForeignKey("Artist", related_name="album_artist", on_delete=models.CASCADE, default='')
    album_image = models.ImageField(blank = True, null=True)
    album_decribe = models.TextField(null=True)
    album_music = models.ManyToManyField(Music)

    def __str__(self):
        return self.album_name

class PlayList(models.Model):
    list_no = models.AutoField(primary_key=True)
    user_no = models.ForeignKey("users.User", related_name = "playlist_user_no", on_delete=models.CASCADE, null=True)
    music_no = models.ForeignKey("Music", related_name = "playlist_music_no", on_delete=models.CASCADE, null=True)
    

    def get_music_no(self):
        return self.music_no

    def __str__(self):
        return f'{self.user_no} playlist'