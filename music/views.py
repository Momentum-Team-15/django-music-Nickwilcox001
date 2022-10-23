from django.shortcuts import render, redirect
from .models import Album
from django.utils import timezone
from music.forms import AlbumForm


# Create your views here.
def index(request):
    albums = Album.objects.order_by('created_at')
    return render(request, 'music/index.html', {'albums': albums})

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect("home")
    else:
        form = AlbumForm()

    return render(request,'music/create_album.html', {'form':form})

def view_albums(request):
    albums = Album.objects.order_by('created_at')
    return render(request,'music/view_albums.html', {'albums': albums})

def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    album.delete()
    return redirect("home")
 
def edit_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    form = AlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        album = form.save()
        return redirect("home")
    return render(request,'music/edit_album.html', {'album': album, 'form': form})
    