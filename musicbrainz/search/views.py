from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .serializers import releaseGroupSerializer

# Create your views here.


class releaseGroupView(views.APIView):

    def get(self, request):
        group_data= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = releaseGroupSerializer(group_data, many=True).data
        return Response(results)
