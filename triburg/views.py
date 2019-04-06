from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.views.generic import TemplateView

def redirectview(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return redirect('/login')



def homepage(request):
    return HttpResponse("<h1>This is home page</h1>")

class Loginpage(TemplateView):
    template = 'login.html'
    def get(self, request, *wargs, **kwargs):
        args = {}
        return render(request,self.template,args)
