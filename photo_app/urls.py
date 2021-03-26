from django.urls import path
from .views import Index, Img_details, Signup, Login, Logout, Post_img, Search

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('img_details/<int:pk>', Img_details.as_view(), name="img_details"),
    path('signup', Signup.as_view(), name="signup"),
    path('login', Login.as_view(), name="login"),
    path('logout', Logout.as_view(), name="logout"),
    path('post_img', Post_img.as_view(), name="post_img"),
    path('search', Search.as_view(), name="search")
]