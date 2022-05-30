from datetime import datetime
from django.http import JsonResponse
from .models import Farmstead, Produce, WeeklyBox
from .serializers import FarmsteadSerializer, ProduceSerializer, WeeklyBoxSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
import pytz
from dotenv import load_dotenv
import os


load_dotenv()

def authenticate(token):
    if token != os.getenv('TOKEN'):
        return False
    else:
        return True

class FarmsteadViewSet(viewsets.ModelViewSet):
    queryset = Farmstead.objects.all()
    serializer_class = FarmsteadSerializer

class ProduceViewSet(viewsets.ModelViewSet):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer

class WeeklyBoxViewSet(viewsets.ModelViewSet):
    queryset = WeeklyBox.objects.all()
    serializer_class = WeeklyBoxSerializer

#######
#Farmstead calls
#######

class GetAllFarms(APIView):
    #Return all farmsteads
    #with no filter return all farmstead information
    #with filter query (eg name, id, region) rerturn only filtered informtion
    def get(self, request):
        if not authenticate(request.headers.get('Authorization')):
            return JsonResponse({
            'HTTP status code': '401',
            'Date': datetime.now(),
            'message': 'Unauthorized'
        })
        if 'filter' in request.GET:
            farmstead_info = list(Farmstead.objects.values(request.GET['filter']))  
        else:
            farmstead_info = list(Farmstead.objects.values())
        return JsonResponse(farmstead_info, safe=False)

class GetSingleFarm(APIView):
    #Return all info on a single farm
    #farm must be determined with name query
    def get(self, request):
        if not authenticate(request.headers.get('Authorization')):
            return JsonResponse({
            'HTTP status code': '401',
            'Date': datetime.now(),
            'message': 'Unauthorized'
        })
        if 'name' in request.GET:
            farmsteads = Farmstead.objects.values()
            selected_farm = farmsteads.get(name=request.GET['name'])

            selected_farm_for_produce = Farmstead.objects.all().get(name=request.GET['name'])
            produce_items = list(selected_farm_for_produce.produces.all())
            produce_names = []
            for produce in produce_items:
                produce_names.append(produce.name)
            selected_farm['produce'] = produce_names
            
        else:
            return JsonResponse('invalid, please use name', safe=False)
        return JsonResponse(selected_farm, safe=False)

class GetFarmsteadImageUrl(APIView):
    #return img url for farmers image
    def get(self, request):
        if not authenticate(request.headers.get('Authorization')):
            return JsonResponse({
            'HTTP status code': '401',
            'Date': datetime.now(),
            'message': 'Unauthorized'
        })
        selected_farmstead = Farmstead.objects.get(name = request.GET['name'])
        return JsonResponse(selected_farmstead.image.url, safe=False)

#######
#Produce calls
#######

class GetAllProduce(APIView):
    #get all produce and return as json
    #Return all produce
    #with no filter return all produce information
    #with filter query (eg name, id, category) rerturn only filtered informtion
    def get(self, request):
        if not authenticate(request.headers.get('Authorization')):
            return JsonResponse({
            'HTTP status code': '401',
            'Date': datetime.now(),
            'message': 'Unauthorized'
        })
        if 'filter' in request.GET:
            produce_List = list(Produce.objects.values(request.GET['filter']))
        else:
            produce_List = list(Produce.objects.values())
        return JsonResponse(produce_List, safe=False)

class GetSingleProduce(APIView):
    #Return all info on a single produce
    #produce must be determined with name query
    def get(self, request):
        if not authenticate(request.headers.get('Authorization')):
            return JsonResponse({
            'HTTP status code': '401',
            'Date': datetime.now(),
            'message': 'Unauthorized'
        })
        if 'name' in request.GET:
            produce = Produce.objects.values()
            selected_produce = produce.get(name=request.GET['name'])
            pics = Produce.objects.all()
            print(pics)
        else:
            return JsonResponse('invalid, please use name', safe=False)
        return JsonResponse(selected_produce, safe=False)

class GetProduceFromCategory(APIView):
    #Return all produce from a selected category
    #produce must be determined with category query
    def get(self, request):
        if not authenticate(request.headers.get('Authorization')):
            return JsonResponse({
            'HTTP status code': '401',
            'Date': datetime.now(),
            'message': 'Unauthorized'
        })
        if 'category' in request.GET:
            produce = Produce.objects.values()
            selected_produce = list(produce.filter(category=request.GET['category']))
        else:
            return JsonResponse('invalid, please use category: Vegetable, Fruits, Other', safe=False)
        return JsonResponse(selected_produce, safe=False)

class GetProduceImageUrl(APIView):
    #return img url for produce image
    def get(self, request):
        if not authenticate(request.headers.get('Authorization')):
            return JsonResponse({
            'HTTP status code': '401',
            'Date': datetime.now(),
            'message': 'Unauthorized'
        })
        selected_produce = Produce.objects.get(name = request.GET['name'])
        return JsonResponse(selected_produce.image.url, safe=False)

#######
#Weekly box calls
#######

class GetWeeklyBox(APIView):
    #return json from weely box
    def get(self, request): 
        if not authenticate(request.headers.get('Authorization')):
            return JsonResponse({
            'HTTP status code': '401',
            'Date': datetime.now(),
            'message': 'Unauthorized'
        })
        #Get weekly boxes filtered by the selected day
        weekly_box_list = WeeklyBox.objects.filter(day = request.GET['day'])
        #Filter list again by the region selected
        weekly_box_list_again = weekly_box_list.filter(region = request.GET['region'])
        #take only the most recent entry from filtered list
        chosen_box = weekly_box_list_again.last()
        #get nz timezone 
        timezone = pytz.timezone('Pacific/Auckland')
        #get time difference between current time and boxes date issued
        time_difference = datetime.now(timezone) - chosen_box.date_issued
        #check if box was created in the last 6 days 
        if time_difference.days < 6:
            return JsonResponse(chosen_box.produce, safe=False)  
        else: 
            return JsonResponse('No box on this day for this region', safe=False)

class GetBoxesOnDate(APIView):
    #return json of weely boxes on a specific date
    def get(self, request):
        if not authenticate(request.headers.get('Authorization')):
            return JsonResponse({
            'HTTP status code': '401',
            'Date': datetime.now(),
            'message': 'Unauthorized'
        })
        #Get all weekly box values
        weekly_box_list = WeeklyBox.objects.values()
        #filter entries by the selected date
        weekly_box_filtered = list(weekly_box_list.filter(date_issued = request.GET['date']))
        return JsonResponse(weekly_box_filtered, safe=False)

class GetBoxesBetweenDates(APIView):
    #return json from weely boxes on a specific date
    def get(self, request):
        if not authenticate(request.headers.get('Authorization')):
            return JsonResponse({
            'HTTP status code': '401',
            'Date': datetime.now(),
            'message': 'Unauthorized'
        })
        #Get all weekly box values
        weekly_box_list = WeeklyBox.objects.values()
        #Get start and end dates from query
        start_date = request.GET['startdate']
        end_date = request.GET['enddate']
        #filter list to contain only entires within range
        weekly_box_filtered = list(weekly_box_list.filter(date_issued__range=[start_date, end_date]))
        return JsonResponse(weekly_box_filtered, safe=False)
