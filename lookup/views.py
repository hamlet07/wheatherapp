from django.shortcuts import render
from requests.api import post

def home(request):
    import json
    import requests
    from datetime import datetime, timezone, timedelta

    city_code = '276594'
    city = 'Poznań'

    if request.method == "POST":
        city = request.POST.get('city')
        if city == 'Poznań':
            city_code = '276594'
        elif city == 'Białystok':
            city_code = '275110'
        elif city == 'Bydgoszcz':
            city_code = '273875'
        elif city == 'Częstochowa':
            city_code = '275785'
        elif city == 'Gdańsk':
            city_code = '275174'
        elif city == 'Gorzów Wielkopolski':
            city_code = '274270'
        elif city == 'Katowice':
            city_code = '275781'
        elif city == 'Koszalin':
            city_code = '276656'
        elif city == 'Kraków':
            city_code = '274455'
        elif city == 'Lublin':
            city_code = '274231'
        elif city == 'Łódź':
            city_code = '274340'
        elif city == 'Olsztyn':
            city_code = '266361'
        elif city == 'Rzeszów':
            city_code = '265516'
        elif city == 'Szczecin':
            city_code = '276655'
        elif city == 'Warszawa':
            city_code = '274663'
        elif city == 'Wrocław':
            city_code = '273125'
        elif city == 'Zielona Góra':
            city_code = '274269'
        else: city_code = '276594'
        #return render(request, 'home.html', {'city': city, 'city_code': city_code})
    
    api_request = requests.get("http://dataservice.accuweather.com/currentconditions/v1/" + city_code + "?apikey=l4sSCFpiMOGuYpdVWHH4yXmFauJGy2rs&language=pl-pl&details=True")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    dt = datetime.fromisoformat(api[0]['LocalObservationDateTime']).astimezone(timezone.utc) + timedelta(hours=2)
    date_time = dt.strftime('%Y-%m-%d %H:%M:%S')

    if api[0]['IsDayTime'] == True:
        day_color = 'day'
    else: day_color = "night"

    if api[0]['WeatherIcon'] <= 3:
        category_color = 'clear'
    elif (api[0]['WeatherIcon'] >= 4)&(api[0]['WeatherIcon'] <=11):
        category_color = 'cloudy'
    elif (api[0]['WeatherIcon'] >= 12)&(api[0]['WeatherIcon'] <=29):
        category_color = 'fall'
    elif api[0]['WeatherIcon'] == 30:
        category_color = 'hot'
    elif api[0]['WeatherIcon'] == 31:
        category_color = 'cold'
    elif api[0]['WeatherIcon'] == 32:
        category_color = 'windy'
    elif (api[0]['WeatherIcon'] >= 33)&(api[0]['WeatherIcon'] <=35):
        category_color = 'clear'
    elif (api[0]['WeatherIcon'] >= 36)&(api[0]['WeatherIcon'] <=38):
        category_color = 'cloudy'
    elif (api[0]['WeatherIcon'] >= 39)&(api[0]['WeatherIcon'] <=44):
        category_color = 'cloudy'
    else: category_color = 'neutral'
        
    return render(request, 'home.html', {'api': api, 'date_time': date_time , 'day_color': day_color,
                        'category_color': category_color, 'city': city, 'city_code': city_code})

def about(request):
    return render(request, 'about.html', {})
