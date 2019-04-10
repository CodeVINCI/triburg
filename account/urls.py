from django.urls import path
from .views import CreateSheet

urlpatterns = [
path('createcostsheet/', CreateSheet.as_view()),
]