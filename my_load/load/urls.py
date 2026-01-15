from django.urls import path

from .views import HomePageView, CreatePostView, IndexPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('post/', CreatePostView.as_view(), name="post"),
    path('index', IndexPageView.as_view(), name="index"),
]