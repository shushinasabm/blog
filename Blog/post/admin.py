from django.contrib import admin

from post.models import Post,AboutUs
#modules
class postAdmin(admin.ModelAdmin):
    list_display=('title','slug','published_at','status')
    list_filter = ('published_at','status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('status','published_at')
class aboutusAdmin(admin.ModelAdmin):
    list_display=('title','email','phone')

# Register your models here.
admin.site.register(Post,postAdmin)
admin.site.register(AboutUs,aboutusAdmin)