from django.shortcuts import render

def home(request):
    import json
    import requests

    api_request = requests.get("http://dataservice.accuweather.com/currentconditions/v1/276594?apikey=l4sSCFpiMOGuYpdVWHH4yXmFauJGy2rs&language=pl-pl&details=True")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
    
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
