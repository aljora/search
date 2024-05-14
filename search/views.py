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
    title = omdb.title(query, tomatoes=True)
    match title["type"]:
        case "series":
            return render(request, 'search/search.html', {
                'query': query,
                'title': title,
            })
        case "movie" | _:
            return render(request, 'search/search.html', {
                'query': query,
                'title': title,
            })
