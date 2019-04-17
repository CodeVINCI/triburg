from django.urls import path
from .views import CreateSheet,PreviewSheet

urlpatterns = [
path('createcostsheet/', CreateSheet.as_view()),
path('previewcostsheet/', PreviewSheet.as_view()),
]
