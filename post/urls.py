from django.urls import path
from .views import test , post
 
#post path
urlpatterns = [
    path('test/',test, name='test' ),
    #هر چیزی که اضافه میکنیم تابع مورد نظر برگردون
    path('post/', post, name= 'post')


    
]
