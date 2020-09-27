from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

from app.imageprocessing.backgroundSub import showNumToReact


# def getPeopleCount(request):
#     temp = showNumToReact()

#     template = loader.get_template('public/index.html')
#     context = {
#         'x': temp['x'],
#         'y': temp['y'],
#         'z': temp['z'],
#         'xyz': temp['xyz']
#     }

#     return HttpResponse(template.render(context, request))
