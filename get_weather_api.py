import datetime
import requests as r


def get_current_temperature(city):
   print("---------------------------------")
   data =r.get(f"http://api.weatherapi.com/v1/current.json?key=cd0e434217644e81903133101220112 &q={city}&aqi=no")
   data=data.json()
   ch = input("Enter f for Fahrenheit and c for Celsius : ")
   while not ch.isalpha():
       print("please enter valid")
       ch = input("Enter f for Fahrenheit and c for Celsius : ")
   ch.lower()
   if ch == "c":
        temp=data['current']['temp_c']
        print(f"{city}'s current temprature : {temp} C")
   elif ch=="f":
           temp = data['current']['temp_f']
           print(f"{city}'s current temprature : {temp} F")
   else:
       print("invalid")


def get_temperature_after(city,no):
    print("---------------------------------")
    data = r.get(f"http://api.weatherapi.com/v1/forecast.json?key=cd0e434217644e81903133101220112 &q={city}&days={no}&aqi=no")
    data = data.json()
    today= datetime.date.today()
    newdate=today+datetime.timedelta(days=no)
    newdate=newdate.strftime("%Y-%m-%d")
    days=data['forecast']['forecastday']
    for day in days:
        if day['date']==newdate:
            ch=input("Enter f for Fahrenheit and c for Celsius : ")
            while not ch.isalpha():
                print("please enter valid")
                ch = input("Enter f for Fahrenheit and c for Celsius : ")
            ch.lower()
            if ch not in ["c","f"]:
                print("invalid")
            if ch=="c":
                print(f"max temp for {city} after {no} days :{day['day']['maxtemp_c']} C")
                print(f"min temp for {city} after {no} days :{day['day']['mintemp_c']} C")
                print(f"avg temp for {city} after {no} days :{day['day']['avgtemp_c']} C")
            elif ch=="f":
                print(f"max temp for {city} after {no} days :{day['day']['maxtemp_f']} F")
                print(f"min temp for {city} after {no} days :{day['day']['mintemp_f']} F")
                print(f"avg temp for {city} after {no} days :{day['day']['avgtemp_f']} F")





def get_lat_and_long(city):
    print("---------------------------------")
    data = r.get(f"http://api.weatherapi.com/v1/current.json?key=cd0e434217644e81903133101220112 &q={city}&aqi=no")
    data = data.json()
    lat = data['location']['lat']
    lon = data['location']['lon']
    print(f"{city}'s latitude : {lat}")
    print(f"{city}'s longitude : {lon}")


get_current_temperature("tokyo")
get_temperature_after("tokyo",4)
get_lat_and_long("tokyo")