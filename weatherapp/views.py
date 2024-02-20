from django.shortcuts import render
import json
import urllib

def index(request):
    if request.method =="POST":
        city = request.POST.get('city')
        url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid=ff6be8c1cc621afbe9c6e34161622f78').read()
        da= json.loads(url)   
        data = {
            'city': city,
         'weather_d' :da['weather'][0]['description'],
         'weather_t' :da['main']['temp'],
         'weather_p':da['main']['pressure'],
         'weather_h' :da['main']['humidity'],
         'weather_speed':da['wind']['speed']   
        }       
    else :  
        data = {
         'city': None,
         'weather_d' :None,
         'weather_t' :None,
         'weather_p':None,
         'weather_h' :None,
         'weather_speed':None,  
        }        
    return render(request,'index.html',{'data':data})