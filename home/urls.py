from django.urls import path
from . import views

urlpatterns = [
	path('', views.base, name='home'),
	path('get_mandi_data_1_year', views.get_mandi_data_1_year, name="get_mandi_data_1_year")
]
