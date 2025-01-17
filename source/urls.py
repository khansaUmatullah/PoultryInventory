from django.urls import path

from source.REST_APIs import ChickenManagementView , ChickenUpdateView , EggListView , ChickenHealthStatus , TotalEggs , \
    EggsLastSevenDays
from . import chicken_views,egg_views
urlpatterns = [

    ### These 3 are REST APIs views
    path ( 'Chicken/' , ChickenManagementView.as_view ( ) , name = 'chicken_list' ) ,
    path ( 'Chicken/<int:pk>' , ChickenUpdateView.as_view ( ) , name = 'chicken_update' ) ,
    path ( 'Egg/' , EggListView.as_view ( ) , name = 'egg_list' ),

    #####  CASE STUDY 3. CRUD Functionality

    path ( 'chickens/' , chicken_views.chicken_list , name = 'chicken_list' ) ,
    path ( 'chickens/add/' , chicken_views.add_chicken , name = 'add_chicken' ) ,
    path ( 'chickens/edit/<int:pk>/' , chicken_views.edit_chicken , name = 'edit_chicken' ) ,
    path ( 'chickens/delete/<int:pk>/' , chicken_views.delete_chicken , name = 'delete_chicken' ) ,

    path ( 'eggs/' , egg_views.egg_list , name = 'egg_list' ) ,
    path ( 'eggs/add/<int:chicken_id>/' , egg_views.add_eggs , name = 'add_eggs' ) ,

#####  CASE STUDY 4. Queries
    path('chickens/health-status/' , ChickenHealthStatus.as_view() , name = 'chicken_by_health_status'),
    path('total/eggs/<int:chicken_id>' , TotalEggs.as_view() , name = 'total_eggs_specific_chicken'),
    path('total/eggs/' , EggsLastSevenDays.as_view() , name = 'total_eggs_last_seven_Days'),
]
