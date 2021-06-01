from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Author
from rest_framework.response import Response
import requests
import uuid
from .serializer import AuthorSerializer

GOOGLE_ANALYTICS_ENDPOINT = "https://www.google-analytics.com/collect"

TRACKER_ID = "G-46CFX2E2PH"

def send_tracking_data(data):
    return requests.post(
        GOOGLE_ANALYTICS_ENDPOINT,
        params=data
    )



class AuthorView(APIView):

    def get(self, req):
        data = Author.objects.all()
        serializer = AuthorSerializer(data, many=True)

        return Response(serializer.data, status=200)

    def post(self, req):

        serializer = AuthorSerializer(data=req.data)

        if not serializer.is_valid():
            return Response({"message":"not valid"}, status=400)
        
        serializer.save()

        data = {
            "cid":str(uuid.uuid4()),
            "tid":TRACKER_ID,
            "uip":req.META.get("REMOTE_ADDR"),
            "hitType": 'event',
            "eventCategory": 'Authors',
            "eventAction": 'create',
            "eventLabel": 'created Author'
        }

        res = send_tracking_data(data)
        print("res", res)

        return Response({"message":"author created"},status=200)