#API : e41afb1406bbd5f67eded588efecc76f : 
from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests 

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config["api_key"]["key"]

def get_weather(city): #for get real-time weather report.
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()#1.city 2.country 3.temp(F) 4.temp(C) 
        city = json["name"]
        country = json["sys"]["country"]
        tempK = json["main"]["temp"]
        tempC = tempK - 273.15
        tempF = (tempK - 273.15)*9/5+32
        final = (city, country, tempC, tempF)
        return final
    else :
        return None

print(get_weather(""))

def searchcity(): #for search a city you want to know the weather.
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl["text"] = "{} : {}".format(weather[0],weather[1])
        temp_lbl["text"] = "{:.2f}°C , {:.2f}°F".format(weather[2],weather[3]) 
    else :
         messagebox.showerror("Try again", "Can't find {} Please try again.".format(city))

#App UI
win = Tk()
win.title("Weather Report App")
win.geometry("400x200")
win.resizable(False,False)

city_text = StringVar()
city_entry = Entry(win, textvariable = city_text , font = (80))
city_entry.pack()

search_btn = Button(win, text = "search" , width = 7 , command = searchcity , font = (80))
search_btn.pack()

location_lbl = Label(win, text = "" , font = (80))
location_lbl.pack()

temp_lbl = Label(win, text = "" , font = (80))
temp_lbl.pack()

win.mainloop()