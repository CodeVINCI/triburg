from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.views.generic import TemplateView
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate

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
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
