from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plot', views.plot, name='plot'),

    # path('getPrice', views.getPrice, name='getPrice')
    path('getDashBoardData', views.getDashBoardData, name='getDashBoardData')
]
