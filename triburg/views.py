from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.views.generic import TemplateView
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from account.models import UserRequest, User

def redirectview(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return redirect('/signup')



def homepage(request):
    return HttpResponse("<h1>This is home page</h1>")


class SignupPage(TemplateView):
    template = 'signup.html'
    def get(self, request, *wargs, **kwargs):
        args = {'form':UserRegistrationForm()}
        return render(request,self.template,args)


    def post(self,request, *wargs, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            user.is_active=False
            user.save()
            r = UserRequest(user=user,permission=None)
            r.save()
            return HttpResponse("<h1>"+username+"</h1><h5>Admin will review your request</h5>")

class SignupRequestpage(TemplateView):
    template_name = 'signuprequests.html'
    def get(self, request, *wargs, **kwargs):
        pending = UserRequest.objects.filter(permission=None)
        args = {"pending_requests":pending}
        return render(request, self.template_name,args)
