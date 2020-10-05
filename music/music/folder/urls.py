from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [  url(r'^$', views.index, name='index'),
	url(r'^artists/$', views.ArtistListView.as_view(), name='artists'),
	url(r'^artists/(?P<pk>\d+)$', views.ArtistDetailView.as_view(), name='artist_detail'),
	url(r'^albums/$', views.AlbumListView.as_view(), name='albums'),
	url(r'^albums/(?P<pk>\d+)$', views.AlbumDetailView.as_view(), name='album_detail'),
	url(r'^albums/(?P<pk>\w)$', views.AlbumDetailView.as_view(), name='album_detail'), 
	url(r'^genres/$', views.GenreListView.as_view(), name='genres'),
	url(r'^genres/(?P<pk>\d+)$', views.GenreDetailView.as_view(), name='genre_detail'),	
	url(r'^genres/(?P<pk>\w)$', views.GenreDetailView.as_view(), name='genre_detail'),	
	url(r'^songs/$', views.SongListView.as_view(), name='songs'),
	url(r'^songs/(?P<pk>\d+)$', views.SongDetailView.as_view(), name='song_detail'),
	url(r'^search-form/', views.search_form),
	url(r'^search/', views.search, name='result'),

]

