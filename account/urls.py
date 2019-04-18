from django.urls import path
from .views import CreateSheet,PreviewSheet,Profile
from . import views

urlpatterns = [
path('createcostsheet/', CreateSheet.as_view()),
path('previewcostsheet/', PreviewSheet.as_view()),
path('profile/', Profile.as_view()),
path('savecostsheet/', views.savecostsheet),
path('sendcostsheet/', views.sendcostsheet),
]
