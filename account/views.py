from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Buyer,Costsheet
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.utils.crypto import get_random_string
# Create your views here.



class CreateSheet(TemplateView):
    template_name = 'createsheet.html'
    def get(self, request, *wargs, **kwargs):
        args = {'buyers': Buyer.objects.all().order_by('buyer_name')}
        return render(request,self.template_name,args)

class PreviewSheet(TemplateView):
    template_name = 'previewsheet.html'
    def get(self, request, *wargs, **kwargs):
        key = request.GET['key']
        sheet = Costsheet.objects.get(key=key)
        args = sheet.sheet
        return render(request,self.template_name,args)

class Profile(TemplateView):
    template_name = 'profile.html'
    def get(self, request, *wargs, **kwargs):
        args = {}
        return render(request,self.template_name,args)

@csrf_exempt
def savecostsheet(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        unique_id = get_random_string(length=32)
        c = Costsheet(creator=request.user,sheet=data,key=unique_id)
        c.save()
        return JsonResponse({"success":1})
    else:
        return JsonResponse({"success":0})
