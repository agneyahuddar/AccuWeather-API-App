import json
#import time
import urllib.request

API="catPCgV9XAGypPyJuqlso2vwvMMPQ9Kp"
print("")
print("The weather information for the next 5 days, for a City in the Country you choose")
print("Please refer to this link for the country codes - https://developer.accuweather.com/countries-by-region")
print("")
countryCode = input("Input the country code - ")
city=input("City Name - ")
print("")

key=""
def askLocation(CountryCode,city):
    searchDest = "http://dataservice.accuweather.com/locations/v1/cities/"+CountryCode+"/search?apikey=catPCgV9XAGypPyJuqlso2vwvMMPQ9Kp&q="+city+"&details=True"
    #print(searchDest)
    with urllib.request.urlopen(searchDest) as searchDest:
        info = json.loads(searchDest.read().decode())
    #print(info)
    destKey=info[0]['Key']
    return(destKey)

def askForecast(destKey):
    dayForecastUrl="http://dataservice.accuweather.com/forecasts/v1/daily/5day/"+destKey+"?apikey=catPCgV9XAGypPyJuqlso2vwvMMPQ9Kp&details=True"
    with urllib.request.urlopen(dayForecastUrl) as dayForecastUrl:
        info = json.loads(dayForecastUrl.read().decode())
    #print(info)
    for key1 in info['DailyForecasts']:
        print("Weather For "+key1['Date'])
        print("Minimum Temp (F) "+str(key1['Temperature']['Minimum']['Value']))
        print("Maximum Temp (F) "+str(key1['Temperature']['Maximum']['Value']))
        print("Day Forecast "+str(key1['Day']['ShortPhrase']))
        print("-----------------------------------------")

key=askLocation(countryCode,city)
askForecast(key)
