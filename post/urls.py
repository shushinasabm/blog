from django.urls import path
from .views import test , post
 
#post path
urlpatterns = [
    path('test/',test, name='test' ),
    path('post/', post, name= 'post')

    
]
