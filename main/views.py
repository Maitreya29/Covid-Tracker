from django.shortcuts import render
import requests
import json
import random
def home(request):

    return render(request, 'home.html')

def info(request, country):
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring = {"country": country}
    countryname=country
    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "yourkeyhere"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    d = response['response']
    s = d[0]

    context = {
        'all': s['cases']['total'],
        'recovered': s['cases']['recovered'],
        'deaths': s['deaths']['total'],
        'new': s['cases']['new'],
        'serious': s['cases']['critical'],
    }
    return render(request, 'index.html', context)



