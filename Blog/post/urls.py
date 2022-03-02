from django.urls import path
from .views import detail, index,contactUs,aboutUs
app_name= "post"
#Post Path
urlpatterns = [
    path('index/',index,name='index'),
    path('contact-us/',contactUs,name='contact-us'),
    path('about-us/',aboutUs,name='about-us'),
    path('detail/<slug:slug>' , detail , name="detail")
]
