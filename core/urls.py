
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path("example/", example),
    path("area/", area),
    path("bar/", bar),
    path("bubble/", bubble),
    path("doughnut/", doughnut),
    path("line/", line),
    path("polar/", polar),
    path("radar/", radar),
    path("scatter/", scatter)
]
