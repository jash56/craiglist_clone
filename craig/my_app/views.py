from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from my_app.models import *

# Create your views here.

CRAIGLIST_URL = "https://mumbai.craigslist.org/search/?query={}"

def home(request):
    return render(request,'base.html' ,{'word': 'JASH'})

def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)
    craig_url = CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(craig_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class' : 'result-row'})
    final_post = []

    for post in post_listings:
        post_title = post.find(class='result-title').txt
        post_url = post.find('a').get('href')
        if post.find(class='result-price'):
            post_price = post.find(class='result-price').txt
        else:
            post_price = 'N/A'
        final_post.append((post_title, post_url, post_price))

    
    context = {
        'search' : search
        'final_post' : final_post
    }
    return render(request, 'my_app/new_search.html', context)
