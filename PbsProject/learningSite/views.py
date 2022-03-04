from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'pages/index.html'

class PythonView(TemplateView):
    template_name = 'pages/python.html'

class ExplanationView(TemplateView):
    template_name= 'pages/explanation.html'

class ListView(TemplateView):
    template_name= 'pages/list.html'

class DatatypeView(TemplateView):
    template_name='pages/datatype.html'

class DataboxView(TemplateView):
    template_name='pages/databox.html'

class ConditionalbranchView(TemplateView):
    template_name='pages/conditionalbranch.html'

class FunctionView(TemplateView):
    template_name='pages/function.html'

class WebapplicationView(TemplateView):
    template_name='pages/webapplication.html'



# Create your views here.
