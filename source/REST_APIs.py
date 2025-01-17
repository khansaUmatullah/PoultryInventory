import datetime

from http import HTTPStatus
from http.client import HTTPResponse

from django.db.models import Count
from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView

from source.models import Chicken, Egg
from source.serializers import ChickenSerializers, EggSerializers


# Create your views here.


class ChickenManagementView(APIView):

    def get(self,request):

        chicken=Chicken.objects.all()
        serialized_data=ChickenSerializers(chicken,many=True)
        return Response(status=HTTPStatus.OK,data=serialized_data.data)

    def post(self,request):
        serializer=ChickenSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTPStatus.CREATED,data=serializer.data)
        return Response(status=HTTPStatus.BAD_REQUEST,data=serializer.errors)

class ChickenUpdateView(APIView):
    def patch(self, request, pk):
        try:
            chicken = Chicken.objects.get(pk=pk)
        except Chicken.DoesNotExist:
            return Response({"error": "Chicken not found"}, status=HTTPStatus.NOT_FOUND)
        serializer = ChickenSerializers(chicken, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTPStatus.OK, data=serializer.data)
        return Response(status=HTTPStatus.BAD_REQUEST, data=serializer.errors)


    def delete(self, request, pk):
        try:
            chicken = Chicken.objects.get(pk=pk)
        except Chicken.DoesNotExist:
            return Response({"error": "Chicken not found"}, status=HTTPStatus.NOT_FOUND)

        chicken.delete()
        return Response({"message": "Chicken deleted successfully"},status=HTTPStatus.NO_CONTENT)



class EggListView(APIView):

    def get(self,request):
        chicken=Egg.objects.all()
        serialized_data=EggSerializers(chicken,many=True)
        return Response(status=HTTPStatus.OK,data=serialized_data.data)

    def post(self,request):
        try:
            Chicken.objects.get(id=request.data['chicken'])
        except Chicken.DoesNotExist:
            return Response ( {"message":'this Chicken does not exist'},status = HTTPStatus.BAD_REQUEST ,)
        serializer=EggSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTPStatus.CREATED)
        return Response ( status = HTTPStatus.BAD_REQUEST , data = serializer.errors )

#####  CASE STUDY 4. Queries

class ChickenHealthStatus(APIView):
    def get(self,request):
        data=Chicken.objects.values('health_status').annotate(total_chicken=Count('id'))
        return Response ( status = HTTPStatus.OK ,data=data)



class TotalEggs(APIView):
    def get(self,request,chicken_id):
        data=Egg.objects.filter(chicken = chicken_id ).aggregate(total_eggs=Sum('quantity'))
        return Response ( status = HTTPStatus.OK , data = data )

class EggsLastSevenDays(APIView):
    def get(self,request):
        now=timezone.now()
        date_seven_days=now-datetime.timedelta(days=7)
        data=Egg.objects.filter( date_collected__range = [date_seven_days,now]).aggregate(total_eggs=Sum('quantity'))
        return Response ( status = HTTPStatus.OK , data = data )







