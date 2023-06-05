# mysite/urls.py
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("chat/", include("chat.urls"), name="chat_index"),
    path("admin/", admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]

from chat.views import index
urlpatterns += path("", index),