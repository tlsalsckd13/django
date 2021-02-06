from django.shortcuts import render, redirect
from blog.models import Category, Music, Artist, Album, PlayList
from users.models import User
# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context=context)

def single(request):
    album_list = Album.objects.all()
    context = {"album_list": album_list }
    return render(request, 'single.html', context= context)

def chart(request) : #curr_page : 현재 페이지
    music_list = Music.objects.all()
    print(music_list)
    context = {"music_list" : music_list}
    return render(request, "chart.html", context )

def playlist(request):
    user_playlist = PlayList.objects.filter(user_no=request.user)
    musics = []
    for i in user_playlist:
        music = i.get_music_no()
        musics.append(Music.objects.filter(music_name=music))

    return render(request, 'playlist.html',{"play_list" : musics})

def list_add(request, music_no):
    user_no = request.user
    list_music_no = Music.objects.get(pk = music_no)
    my_list = PlayList(user_no = user_no, music_no=list_music_no)
    my_list.save()

    return redirect("/blog/playlist")

def list_delete(request, music_no):
    user_no = request.user
    list_music_no = Music.objects.get(pk = music_no)
    my_list = PlayList.objects.filter(music_no = list_music_no)
    my_list.delete()
    return redirect("/blog/playlist")

def albumdetail(request, list_id):
    
    albumdetail = Album.objects.get(pk = list_id)
    context = {"albumdetail": albumdetail}

    return render(request, "albumdetail.html", context)


def musicdetail(request, list_id):

    musicdetail = Music.objects.get(pk = list_id)
    context = {"musicdetail" : albumdetail}

    return render(request, "musicdetail.html", context)