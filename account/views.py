from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Buyer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.



class CreateSheet(TemplateView):
    template_name = 'createsheet.html'
    def get(self, request, *wargs, **kwargs):
        args = {'buyers': Buyer.objects.all().order_by('buyer_name')}
        return render(request,self.template_name,args)

class PreviewSheet(TemplateView):
    template_name = 'previewsheet.html'
    def get(self, request, *wargs, **kwargs):
        args = {}
        return render(request,self.template_name,args)

class Profile(TemplateView):
    template_name = 'profile.html'
    def get(self, request, *wargs, **kwargs):
        args = {}
        return render(request,self.template_name,args)

@csrf_exempt
def savecostsheet(request):
    if request.method == 'POST':
        knitfabricdata = request.POST.get('knitfabricdata',[])
        JsonResponse({"success":1})
