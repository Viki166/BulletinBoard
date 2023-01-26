from django.urls import path
from Main.views import ContactView





urlpatterns = [

    path("", ContactView.as_view(),name="contact"),

]