from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Buyer
# Create your views here.



class CreateSheet(TemplateView):
    template_name = 'createsheet.html'
    def get(self, request, *wargs, **kwargs):
        args = {'buyers': Buyer.objects.all()}
        return render(request,self.template_name,args)
