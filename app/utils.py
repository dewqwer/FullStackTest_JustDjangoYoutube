# from .serializer import UserSerializer

from .model.people_counter.graduation_ceremony.V9_1 import people_main
import asyncio
import datetime
import random
import websockets
import json



# def my_jwt_response_handler(token, user=None, request=None):
#     return {
#         'token': token,
#         'user': UserSerializer(user, context={'request': request}).data
#     }



def realTimeNum():
    # return JsonResponse(count_model)

    people = people_main.PeopleCounter()
    people_count = people.people_count

    while True:
        
        now = datetime.datetime.utcnow().isoformat()
        count_model = {
            "people_count": str(people_count),
            "time": str(now),
        }

    return json.dumps(count_model)