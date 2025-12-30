from django.urls import re_path
from django.contrib import admin

urlpatterns = [
    # Examples for custom menu
    re_path(r"^foo/bar/", admin.site.urls),
]
