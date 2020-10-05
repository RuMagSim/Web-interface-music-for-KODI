# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.urls import reverse 




class Artist(models.Model):
    name_artist= models.CharField(max_length=250, db_column='strArtist', help_text="Исполнитель") 
    art = models.ForeignKey("Art", to_field='art', db_column='idArtist', unique=True, primary_key=True )
    genre_artist = models.TextField(db_column='strGenres', help_text="Жанр")   
 
    def __unicode__(self):
        return self.name_artist
	    
    def get_absolute_url(self):
        return reverse('artist_detail', args=[str(self.pk)])
     
    class Meta:
        db_table = 'artist'
        ordering = ["name_artist"]
		
        
class Album(models.Model):
    album_id = models.AutoField( db_column='idAlbum', primary_key=True)
    members = models.ManyToManyField(Artist, through='Membership')
    name_album = models.CharField(max_length=250, db_column='strAlbum', help_text="")
    artists = models.CharField(max_length=250, db_column='strArtists', help_text="") 
    #artist= models.ForeignKey(Artist, to_field='artist_id', related_name = '+')
    year = models.IntegerField(db_column='iYear')
    name_genre = models.CharField(max_length=250, db_column='strGenres')
    #art = models.IntegerField( db_column='idAlbum', primary_key=True)
    m3u = models.CharField(max_length=250, db_column='strImage')
    rating = models.IntegerField(db_column='iUserrating')
    label = models.CharField(max_length=250, db_column='strLabel')
	
    def __unicode__(self): 
        return self.name_album

    def get_absolute_url(self):
        return reverse('album_detail', args=[str(self.pk)])		
		
    class Meta:
       db_table = 'album' 
       ordering = ["year"]
	   
	
class Membership(models.Model):
    artist = models.ForeignKey(Artist, db_column='idArtist', primary_key=True, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, db_column='idAlbum', primary_key=True, on_delete=models.CASCADE)
    name_artist = models.IntegerField(db_column='strArtist')  
          		  
    class Meta:
       db_table = 'album_artist' 
	   
    def __unicode__(self):
        return self.name_artist
	    
    def get_absolute_url(self):
        return reverse('artist_detail', args=[str(self.pk)])	   

	   	   
class Song(models.Model):
    song_id = models.AutoField(db_column='idSong',unique=True, primary_key=True)
    album = models.ForeignKey(Album, Artist, db_column='idAlbum')
    #id_album = models.IntegerField (db_column='idAlbum')
    members = models.ManyToManyField(Artist, through='Membership2')
    path = models.OneToOneField("Path", db_column='idPath')
    name_artists = models.CharField(max_length=250, db_column='strArtists', help_text="Исполнитель")
    genres = models.CharField(max_length=250, db_column='strGenres', help_text="Жанр")
    title = models.CharField(max_length=250, db_column='strTitle', help_text="Трек")
    track = models.IntegerField(db_column='iTrack', help_text="Номер трека")  
    duration = models.IntegerField(db_column='iDuration') 
    year = models.IntegerField(db_column='iYear',help_text="Год")  
    file_name = models.FileField(db_column='strFileName', help_text="Файл")
    comment = models.TextField (db_column='comment')
	
    def __unicode__(self):
        return self.title
		
    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.pk)])			

    class Meta:
	    db_table = 'song'
	    ordering = ["track"]
		
		
class Membership2(models.Model):
    artist = models.ForeignKey(Artist, db_column='idArtist', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, db_column='idSong', on_delete=models.CASCADE)
	   
    class Meta:
       db_table = 'song_artist' 		
	
	
class Genre(models.Model):
    genre_id = models.AutoField(db_column='idGenre', primary_key=True)
    members = models.ManyToManyField(Album, through='Membership3') 
    name_genre= models.CharField(max_length=250, db_column='strGenre', help_text="Жанр")
	
    def __unicode__(self):
        return self.name_genre
	
    def get_absolute_url(self):
        return reverse('genre_detail', args=[str(self.pk)])

    class Meta:
	    db_table = 'genre'
	    ordering = ["name_genre"]	    
	
		
class Membership3(models.Model):
    genre = models.ForeignKey("Genre", db_column='idGenre', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, db_column='idAlbum', on_delete=models.CASCADE)
	   
    class Meta:
       db_table = 'album_genre'           		  
		
		
class Art (models.Model):
    id = models.AutoField(db_column='art_id', primary_key=True)
    art = models.ForeignKey("Album", to_field='album_id', db_column='media_id')
    art_artist = models.ForeignKey("Artist", db_column='media_id', related_name='art_artist') 
     # = models.ForeignKey("Artist")
    media_type = models.CharField(max_length=250, db_column='media_type', help_text="Трек,Альбом")
    type = models.CharField(max_length=250, db_column='type', help_text="Тип")
    image = models.ImageField(db_column='url')
    
	
    def __unicode__(self):
        return self.image.name
    
    def get_absolute_url(self):
        return reverse('artist_detail', args=[str(self.image)])		

    class Meta:
	    db_table = 'art'
   

class Path(models.Model):
    path_id = models.AutoField(db_column='idPath', primary_key=True)
    strpath =  models.CharField(max_length=250, db_column='strPath', help_text="Тип")
    hash =  models.TextField(db_column='strHash', help_text="хэш")
    
    def __unicode__(self):
        return self.strpath
		
    class Meta:
	    db_table = 'path'