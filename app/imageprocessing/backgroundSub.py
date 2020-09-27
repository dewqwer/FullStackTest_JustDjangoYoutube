# from django.shortcuts import render


# def showNumToReact():
#     x = 1
#     y = x+10
#     z = x+y+100
#     xyz = x+y+z+1000

#     currentCount = {'x': x,
#                     'y': y,
#                     'z': z,
#                     'xyz': xyz,
#                     }

#     return currentCount


# temp = showNumToReact()
# print(temp)
# print(temp['x'])

# importing the requests library
import requests

# api-endpoint
URL = "http://localhost:8000"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address': location}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)
