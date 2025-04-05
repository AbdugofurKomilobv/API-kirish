from http.client import responses

from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

@api_view(['GET','POST'])
def movie_api(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def movie_detail(request,slug):
    try:
        movie = Movie.objects.get(slug=slug)
        responses = {'success':True}
    except Movie.DoesNotExist:
        responses = {'error': 'Movie not found'}
        return Response(data=responses,status=status.HTTP_404_NOT_FOUND)


    if request.method == "GET":
        serializer = MovieSerializer(movie)
        responses['data'] = serializer.data
        return Response(data=responses,status=status.HTTP_200_OK)


    elif request.method == "PUT":
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            responses['data']=serializer.data
            return Response(data=responses,status=status.HTTP_200_OK)



    elif request.method == "PATCH":
        serializer = MovieSerializer(movie, data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            responses['data'] = serializer.data
            return Response(data=responses, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie.delete()
        responses = {'success':True, 'message': 'Movie deleted successfully'}
        return Response(data=responses,status=status.HTTP_204_NO_CONTENT)

 # actors get,post


# actor_api  bu funksya actor modelni get bilan xammasini koradi post bilan 1 ta malumot qoshadi
@api_view(['GET','POST'])
def actor_api(request):
    if request.method == "GET":
        actor = Actors.objects.all()
        serializer = ActorSerializer(actor,many = True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = ActorSerializer(data = request.data)
        if serializer.is_valid():
         serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH','DELETE'])
def actor_detail(request,pk):
    try:
        actor = Actors.objects.get(pk=pk)
        responses = {'succes':True}
    except Actors.DoesNotExist:
        responses = {'error': 'Actor not found'}
        return Response(data=responses,status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serializer = ActorSerializer(actor)
        responses['data'] = serializer.data
        return Response(data=responses,status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = ActorSerializer(actor,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            responses['data'] = serializer.data
            return Response(data=responses, status=status.HTTP_200_OK)
        
    elif request.method == "PATCH":
        serializer = ActorSerializer(actor,data = request.data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            responses['data'] = serializer.data
            return Response(data=responses,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == "DELETE":
        actor.delete()
        responses = {'success':True, 'message': 'Actor dalete successfully'}
        return Response(data=responses,status=status.HTTP_204_NO_CONTENT)
        
