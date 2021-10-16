from django.shortcuts import render
import os
import omdb

def getsecret(source):
    with open(os.getenv(source)) as keyfile:
        return keyfile.read().rstrip('\n')

omdb.set_default('apikey', getsecret('OMDB_KEY_FILE'))

# Create your views here.

def search(request):
    query = request.GET['q']
    return render(request, 'movie/search.html', {
        'query': query,
        'title': omdb.title(query, tomatoes=True),
        'search': omdb.search_movie(query)
    })
