# blog_api/urls.py

from django.urls import path
# from django.views.generic import TemplateView
from . import views


app_name = 'blog_api'

urlpatterns = [
    # path('', PostList.as_view(), name='listcreate'),
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
]