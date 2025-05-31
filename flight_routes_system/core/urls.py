from django.urls import path
from core import views

urlpatterns = [
    path('', views.landing_view, name='landing_view'),

    # Login page
    path('login', views.login_view, name='login'),

    path('airports/', views.manage_airport, name='manage_airport'),
    path('airports/search', views.search_port, name='search_port'),
    path('airports/longest', views.longest_distance, name='longest_distance'),
    path('airports/shortest', views.shortest_distance, name='shortest_distance'),

]
