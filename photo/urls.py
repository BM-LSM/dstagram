from django.urls import path

from .views import *

# 2차 URL 파일(config에 있는 파일이 1차 파일)
app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('upload/', PhotoUpdateView.as_view(), name="photo_upload"),
]