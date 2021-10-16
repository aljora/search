from django.shortcuts import render
import os
import omdb

def getsecret(source):
    with open(os.getenv(source)) as keyfile:
        return keyfile.read().rstrip('\n')

omdb.set_default('apikey', getsecret('OMDB_KEY_FILE'))

# Create your views here.

def search(request):
    title = request.GET['q']
    print(omdb.search_movie(title))
    return render(request, 'movie/search.html', {'query': title})
