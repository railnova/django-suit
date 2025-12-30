from django.urls import re_path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

urlpatterns = i18n_patterns(
    # Examples for custom menu
    re_path(r"^admin/", admin.site.urls),
)
