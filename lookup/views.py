from django.shortcuts import render
from requests.api import post


def home(request):
    import json
    import requests
    import unicodedata

    city_code = 'poznan'
    city = 'Poznań'

    if request.method == "POST":
        city = request.POST.get('city')
        city_code = city.lower().replace(' ', '').replace('ą', 'a').replace('ę', 'e').replace('ć', 'c').replace('ś', 's').replace('ń', 'n').replace('ó', 'o').replace('ź', 'z').replace('ż', 'z')
    
    api_request = requests.get("https://danepubliczne.imgw.pl/api/data/synop/station/"+ city_code)

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    date_time = api['data_pomiaru']+' '+api['godzina_pomiaru']+'.00'

    if (int(api['godzina_pomiaru'])>=22)&(int(api['godzina_pomiaru'])<=6):
        day_color = 'day'
    else: day_color = "night"
        
    return render(request, 'home.html', {'api': api, 'api_request': api_request,
                        'date_time': date_time , 'day_color': day_color,
                        'city': city, 'city_code': city_code})

def about(request):
    return render(request, 'about.html', {})
