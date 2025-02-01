from django.urls import path
from . import views

urlpatterns = [
    path("", views.LandingPageView.as_view(), name="landing-page"),
    path("/posts", views.AllPostsView.as_view(), name="posts-page"),
    path("/post/<slug:slug>", views.SinglePostView.as_view(),
         name="post-details-page"),
]
