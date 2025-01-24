from django.contrib import admin
from blog.models import PostModel,PostCategory,CommentModel

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_date','status')
    
@admin.register(PostCategory)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_date')
    
@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('post','name','email','message')
