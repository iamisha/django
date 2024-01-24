
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('',views.hello_world),
   path('home/', views.homep)
]
urlpatterns += staticfiles_urlpatterns()