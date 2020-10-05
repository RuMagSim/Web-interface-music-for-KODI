# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Artist, Album, Song, Genre, Art
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import F


def index(request):
    art_list = Art.objects.filter(type='fanart').order_by( '-id') [:1]
    album_list = Album.objects.order_by ('-album_id') [:20]
    album2_list = Album.objects.order_by ('-year') [:20]

    context = {'art_list': art_list,
               'album_list': album_list,
               'album2_list': album2_list,
               }
    return render(request, 'index.html', context)

	
class ArtistListView(generic.ListView):
    model = Artist

    def post (self):
	
      return Artist.objects.filter(membership__name_artist=not True).distinct()
    queryset = Artist.objects.filter(membership__name_artist=not True).distinct()
    template_name  =  'folder/artist_list.html'
	

    
class ArtistDetailView(generic.DetailView):
    model = Artist

    def post (self):
      return Artist.objects.order_by('membership__artist')
    queryset = Artist.objects.order_by('membership__artist')
 
	
    list_display = ('name_album', 'year')
	
    def get_context_data(self, **kwargs):
     context = super(ArtistDetailView, self).get_context_data(**kwargs)
     context['art_list'] = Art.objects.filter(art=self.kwargs.get('pk')).filter(type='fanart')
     return context 

	
class AlbumListView(generic.ListView):
    model = Album
    	
class AlbumDetailView(generic.DetailView):
    model = Album
	
    def get_context_comment(self, **kwargs):
     context = super(AlbumDetailView, self).get_context_data(**kwargs)
     context['song_comment'] = Song.objects.filter(song=self.kwargs.get('pk')) [:1]
     return context
	 
    Album.objects.filter(pk=1).update(rating=F('rating')+1)	
    
	 
class GenreListView(generic.ListView):
    model = Genre

class GenreDetailView(generic.DetailView):
    model = Genre
	
			
class SongListView(generic.ListView):
    model = Song

    def post (self):
     context_object_name  =  'artist_song' 
     return Artist.objects.filter(membership__artist=None)
    queryset = Artist.objects.filter(membership__artist=None)	 
    template_name  =  'folder/song_list.html'
	
    paginate_by = 100
		
class SongDetailView(generic.DetailView):
    model = Song
	
    def post (self):
     context_object_name  =  'artist_song' 
     return Artist.objects.filter(membership__artist=None)
    queryset = Artist.objects.filter(membership__artist=None)
    template_name  =  'folder/song_detail.html'

	
def search_form(request):
    return render_to_response('search_form.html')
	
def search(request):
    if 'q' in request.GET:
        message = 'Поиск: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)	
	
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        songs = Song.objects.filter(title__icontains=q)
        artists = Song.objects.filter(name_artists__icontains=q)
        return render_to_response('search_results.html',
            {'songs': songs, 'artists': artists, 'query': q},)
    else:
        return HttpResponse('Please submit a search term.')	
		
