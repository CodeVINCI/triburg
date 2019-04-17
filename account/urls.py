from django.urls import path
from .views import CreateSheet,PreviewSheet,Profile

urlpatterns = [
path('createcostsheet/', CreateSheet.as_view()),
path('previewcostsheet/', PreviewSheet.as_view()),
path('profile/', Profile.as_view()),
]
