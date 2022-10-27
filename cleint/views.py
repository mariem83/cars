from django.http import HttpResponse
from .models import Client , Car,Company
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CarSer,CompanySer,ClientSer
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the cars index.")
@api_view(['GET'])
def get_car(request):
    cars = Car.objects.all()
    serializer = CarSer(cars, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_cleint(request):
    cleints = Client.objects.all()
    serializer = ClientSer(cleints, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_company(request):
    companys = Company.objects.all()
    serializer = CompanySer(companys, many=True)
    return Response(serializer.data)

