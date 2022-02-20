from pyexpat import model
from turtle import title
from django.contrib import admin
from post.models import Post,aboutus
class postAdmin(admin.ModelAdmin):
    list_display=('title','slug','publish_at','status')
    list_filter =('publish_at','status')
    search_fields =('title','discription')
    prepopulated_fields={'slug':('title',)}
    ordering=('status','publish_at')
# Register your models here.
admin.site.register(Post,postAdmin)

class aboutusadmin(admin.ModelAdmin):
    list_display=('title_us','git_hub_us','tiwtter_us','insta_us')
admin.site.register(aboutus,aboutusadmin)