from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .models import City
from .serializer import CitySerializer
from datetime import datetime
# Create your views here.


class Index(APIView):

    def get(self,request,*args ,**kwargs):
        city = self.kwargs["city"]

        existing_city = City.objects.filter(
            name__icontains=str(city).lower())
        if len(existing_city) == 0:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city.title()}&units=imperial&APPID=d0fc4891729781a0948e979e38a2e847"
            r = requests.get(url).json()
            if r['cod'] == 200:

                rise_time = r['sys']['sunrise']
                
                s_rise = datetime.fromtimestamp(
                    (rise_time)
                ).strftime('%Y-%m-%d %H:%M:%S')

                set_time = r['sys']['sunset']

                s_set = datetime.fromtimestamp(
                    (set_time)
                ).strftime('%Y-%m-%d %H:%M:%S')

                cities = City(name=city.title(),
                            desc=r['weather'][0]['description'],
                            temp_min=r['main']['temp_min'],
                            temp_max=r['main']['temp_max'],
                            pressure=r['main']['pressure'],
                            humidity=r['main']['humidity'],
                            sunrise_time=s_rise,
                            sunset_time=s_set
                            )

                cities.save()
            
                weather = City.objects.filter(name__icontains = str(city).lower())
                if weather:
                    serializer = CitySerializer(weather,many=True)
                    print(1)
                    return Response(serializer.data)
        
        else:   
            b = datetime.now().strftime("%Y-%m-%d")
            
            weather = City.objects.filter(name__icontains = str(city).lower(),  created_at__contains = b )
            if weather:
                serializer = CitySerializer(weather,many=True)
                print(2)
                return Response(serializer.data)

            else:
                
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city.title()}&units=imperial&APPID=d0fc4891729781a0948e979e38a2e847"
                r = requests.get(url).json()
                if r['cod'] == 200:

                    rise_time = r['sys']['sunrise']
        
                    s_rise = datetime.fromtimestamp(
                        (rise_time)
                    ).strftime('%Y-%m-%d %H:%M:%S')

                    set_time = r['sys']['sunset']
                    s_set = datetime.fromtimestamp(
                        (set_time)
                    ).strftime('%Y-%m-%d %H:%M:%S')

                    c = datetime.now().strftime("%Y-%m-%d")

                    weather = City.objects.filter(name__icontains = str(city).lower()).update(
                        desc=r['weather'][0]['description'],
                        temp_min=r['main']['temp_min'],
                        temp_max=r['main']['temp_max'],
                        pressure=r['main']['pressure'],
                        humidity=r['main']['humidity'],
                        sunrise_time=s_rise,
                        sunset_time=s_set,
                        created_at = c
                        )

                    
                    weather = City.objects.filter(name__icontains = str(city).lower())
                    if weather:
                        serializer = CitySerializer(weather,many=True)
                        print(3)
                        return Response(serializer.data)

        return Response({'msg':"Please enter valid city"})



                    

