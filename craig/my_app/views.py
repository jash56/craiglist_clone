from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from my_app.models import *
from datetime import datetime

# Create your views here.

CRAIGLIST_URL = "https://{}.craigslist.org/search/?query={}"
IMAGE_URL = "https://images.craigslist.org/{}_300x300.jpg"

def home(request):
    return render(request,'base.html' ,{'word': 'JASH'})

def new_search(request):
    search = request.POST.get('search')
    area = request.POST.get('area')
    date = datetime.now()
    Search.objects.create(search=search, area=area, created=date)
    craig_url = CRAIGLIST_URL.format(area, quote_plus(search))
    response = requests.get(craig_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class' : 'result-row'})
    final_post = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = IMAGE_URL.format(post_image_id)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        final_post.append((post_title, post_url, post_price, post_image_url))
    
    context = {
        'search' : search,
        'final_post' : final_post
    }
    return render(request, 'my_app/new_search.html', context)