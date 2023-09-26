from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import re_path

admin.autodiscover()

urlpatterns = i18n_patterns('',
    re_path(r'^admin/', admin.site.urls),
)
