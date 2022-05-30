from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from Api.views import FarmsteadViewSet, ProduceViewSet, WeeklyBoxViewSet
from Api.views import GetAllFarms, GetSingleFarm, GetFarmsteadImageUrl
from Api.views import GetAllProduce, GetSingleProduce, GetProduceFromCategory, GetProduceImageUrl
from Api.views import GetWeeklyBox, GetBoxesOnDate, GetBoxesBetweenDates

router = DefaultRouter()
router.register('farmstead', FarmsteadViewSet, basename ='farmstead')
router.register('produce', ProduceViewSet, basename ='produce')
router.register('weeklybox', WeeklyBoxViewSet, basename ='weeklybox')
router.register('currentbox', WeeklyBoxViewSet, basename ='weeklybox')


urlpatterns = [

    re_path(r'^GetProduceImageUrl/$',GetProduceImageUrl.as_view()),
    re_path(r'^GetFarmsteadImageUrl/$',GetFarmsteadImageUrl.as_view()),
    path('', include(router.urls)),
    ######
    #farmstead paths
    ######
    re_path(r'^GetAllFarms/$', GetAllFarms.as_view()),
    re_path(r'^GetSingleFarm/$', GetSingleFarm.as_view()),
    ######
    #produce paths
    ######
    re_path(r'^GetAllProduce/$', GetAllProduce.as_view()),
    re_path(r'^GetSingleProduce/$', GetSingleProduce.as_view()),
    re_path(r'^GetProduceFromCategory/$', GetProduceFromCategory.as_view()),
    ######
    #weeklybox paths
    ######
    re_path(r'^GetWeeklyBox/$', GetWeeklyBox.as_view()),
    re_path(r'^GetBoxesOnDate/$', GetBoxesOnDate.as_view()),
    re_path(r'^GetBoxesBetweenDates/$', GetBoxesBetweenDates.as_view())
]