from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from first.views import Home_Page,Data_Input,Hospital_Data_View
urlpatterns = [
    path('',Home_Page,name='index'),
    path('input/',Data_Input,name="input"),
    path('hospital/',Hospital_Data_View,name="hospital")
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

