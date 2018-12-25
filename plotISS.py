#!/bin/python3

import json
import turtle
import urllib.request
import time

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('People in space: ', result['number'])
people = result['people']

for p in people:
  print(p['name'])

url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print("latitude: ", lat)
print("logitude: ", lon)

# convert file to .gif (50X50 px): https://www.online-convert.com/result/c63f1d0a-b9e4-4468-9a3a-bf556ae7dfae
screen = turtle.Screen()
screen.setup(540, 270)
screen.bgpic("mapp.gif")
screen.setworldcoordinates(-180, -90, 180, 90)

screen.register_shape('meercaa.gif')
iss = turtle
iss.shape('meercaa.gif')
iss.setheading(90)
iss.penup()
iss.goto(float(lon), float(lat))


screen.exitonclick()

# Pasadena, CA http://www.latlong.net/
lat = 34.138
lon = -118.125
location = turtle
# location.penup()
# location.color('yellow')
# location.goto(lon, lat)
# location.dot(5)
# location.hideturtle()

# url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# over = result['response'][1]['risetime']
# # print(over)
# style = ('Arial', 6)
# location.write(time.ctime(over), font=style)

