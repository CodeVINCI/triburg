from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.views.generic import TemplateView
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from account.models import UserRequest, User

def redirectview(request):
    if request.user.is_authenticated:
        return redirect('/accounts/profile')
    else:
        return redirect('/login')



def homepage(request):
    return HttpResponse("<h1>This is home page</h1>")

class SearchUsers(TemplateView):
    template = 'searchusers.html'
    def get(self, request, *wargs, **kwargs):
        if request.user.is_admin:
            query = request.GET['query']
            filter = request.GET['filter']
            users = User.objects.filter(Q(username__contains=query) | Q(first_name__contains=query) | Q(last_name__contains=query) | Q(email__contains=query) |)
            args = {'results':users}
            return render(request,self.template,args)
        else:
            return redirect('/login')

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
        if request.user.is_admin:
            pending = UserRequest.objects.filter(permission=None)
            args = {"pending_requests":pending}
            return render(request, self.template_name,args)
        else:
            return HttpResponse('<h1>Please Log in as the admin</h1>')


def approverequest(request):
    if request.user.is_admin:
        id = request.GET['id']
        r = UserRequest.objects.get(id=id)
        u = r.user
        u.is_active=True;
        u.save()
        r.permission = True;
        r.save()
        return redirect('/signuprequests')
    else:
        return HttpResponse('<h1>Not Admin</h1>')


def disapproverequest(request):
    if request.user.is_admin:
        id = request.GET['id']
        r = UserRequest.objects.get(id=id)
        u = r.user
        u.is_active=False;
        u.save()
        r.permission = False;
        r.save()
        return redirect('/signuprequests')
    else:
        return HttpResponse('<h1>Not Admin</h1>')

def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
