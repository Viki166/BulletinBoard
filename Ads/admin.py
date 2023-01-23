from django.contrib import admin
from Ads.models import Ad, Game, Category, Comment

class AdAdmin(admin.ModelAdmin):
    list_display=('id','header','datetime','category','game')
    list_display_links = ('id','header')
    search_fields = ('header','text')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','text','active')
    list_display_links = ('id','text')
    search_fields = ('text',)


admin.site.register(Ad, AdAdmin)
admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)