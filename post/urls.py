from django.urls import path
from .views import detail, posts, test ,index, aboutus ,contactus
app_name ="post"
 
#post path
urlpatterns = [
    path('test/',test, name='test' ),
    #هر چیزی که اضافه میکنیم تابع مورد نظر برگردون
    path('posts/', posts, name= 'post'),
    path('detail/<slug:slug>',detail, name = 'detail'),
    path('index/',index , name ="main"),
    path('aboutus/',aboutus , name ="aboutus"),
    path('contactus/',contactus , name ="contactus"),

    ]   
