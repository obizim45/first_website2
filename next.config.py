#make sure to pip install all modules below before running code 
import os 
import folium
from folium import plugins
from ipywidgets import widgets, interact_manual
import requests, json 
import earthpy as et
import earthpy.spatial as es
from IPython.display import display, HTML,Image
from googlesearch import search


reply = 'are u bored'
typed = 'your location'
display(HTML(f"<h1>{reply.title()} in {typed}? if so, this program can help you  "))


pic = "https://www.tikvahlake.com/wp-content/uploads/2021/08/Boredom-768x512.jpeg"
display(Image(url=pic,width=200))



Question = input(" Are You Bored? Answer(Yes or No)")
if Question == 'Yes':
    pic = "https://img.freepik.com/premium-psd/it-s-time-travel-motivational-lettering-quote-holidays-traveling-concept_23-2148212942.jpg?w=996"
    display(Image(url=pic,width=200))
    query = input('Search for(Places to Eat, Swim, Watch movies etc..in your location): ')
    api_key = 'AIzaSyBnEIVja3YKgvqGiKXPfaBhdDSIHGHmQXI' 
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"   
    r = requests.get(url + 'query=' + query +
                            '&key=' + api_key)
    x = r.json()
    y = x['results']
    for i in range(len(y)):
        print(y[i]['name'])
if Question != 'Yes':
    print(" Alright Have a Great day, See You When Your Bored")

    
    
    
query = input('(Copy & Paste from above options to get address: ')
url = "https://trueway-places.p.rapidapi.com/FindPlaceByText"
querystring = {"text":query,"language":"en"}
headers = {
    
"X-RapidAPI-Key": "7dc1488745msh22957a537034f18p153195jsn7aa97ee9b1d9",
"X-RapidAPI-Host": "trueway-places.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text) 



query0 = input('write the place name followed by the word (rating): ')
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 #tosearch
query = query0
 
for j in search(query, tld="co.in", num=11, stop=1, pause=2):
    reply = (f'Link to {query0} Rating')
    typed = 'Your Location'
    display(HTML(f"<h1>{reply.title()} in {typed} "))
    print(j)    

    
    
query1 = input("Write 'Direction to' followed by the place name): ")
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

query = query1
 
for i in search(query, tld="co.in", num=1, stop=1, pause=2):
    reply = (f' {query1}')
    typed = 'Below, (click Link) '
    display(HTML(f"<h1>{reply.title()} are {typed} "))
    print(i)


location = input('Current city of your Destination: ')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = location
API_KEY = "f61953d239dbc4451ea159cd0860bf39"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = main['temp']
    temp_feel_like = main['feels_like']  
    humidity = main['humidity']
    pressure = main['pressure']
    weather_report = data['weather']
    wind_report = data['wind']
    print(f" Weather is Looking like in {CITY:-^35}")
    print(f"City ID: {data['id']}")   
    print(f"Temperature: {temperature}")
    print(f"Feel Like: {temp_feel_like}")    
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {weather_report[0]['description']}")
    print(f"Wind Speed: {wind_report['speed']}")
    print(f"Time Zone: {data['timezone']}")
else:
    print("Error in the HTTP request")
    
    
data = et.data.get_data('spatial-vector-lidar')
os.chdir(os.path.join(et.io.HOME, 'earth-analytics', 'data'))
m = folium.Map(location=[43.0481, -76.1474])
print(m)


typed = input('What did you thing of the Program: ')
front = 'Thanks for your '
back = 'hope you come back again'
@interact_manual(reply = typed)
def main(reply):
        display(HTML(f" hope you come back again <h1>{front.title()}{reply.title()} and {back}"))
        reply = typed
        url = 'http://text-processing.com/api/sentiment/'
        payload = { 'text' : reply }
        response = requests.post(url, data = payload)
        sentiment = response.json()
        print("SENTIMENT", sentiment['label'])
        
        
        
