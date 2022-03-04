from django.urls import path
from . import views

app_name ='learningSite'

urlpatterns =[
    path('', views.IndexView.as_view(), name='index'),
    path('python',views.PythonView.as_view(), name='python'),
    path('explanation',views.ExplanationView.as_view(), name='explanation'),
    path('list', views.ListView.as_view(), name='list'),
    path('datatype', views.DatatypeView.as_view(), name='datatype'),
    path('databox', views.DataboxView.as_view(), name='databox'),
    path('conditionalbranch', views.ConditionalbranchView.as_view(), name='conditionalbranch'),
    path('function', views.FunctionView.as_view(), name='function'),
    path('webapplication', views.WebapplicationView.as_view(), name='webapplication'),

]