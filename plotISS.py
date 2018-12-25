#!/bin/python3

import json
import turtle
import urllib.request
import turtle
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

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.jpg')

screen.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)
iss.penup()
iss.goto(lon, lat)

# Pasadena, CA http://www.latlong.net/
lat = 34.138
lon = -118.125
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']
# print(over)
style = ('Arial', 6, 'Bold')
location.write(time.ctime(over), font=style)

