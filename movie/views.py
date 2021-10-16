from django.shortcuts import render
import os

def getsecret(source):
    with open(os.getenv(source)) as keyfile:
        return keyfile.read().rstrip('\n')

OMDB_KEY = getsecret('OMDB_KEY_FILE')

# Create your views here.

def search(request):
    return render(request, 'movie/search.html', {'query': request.GET['q']})
