from django.contrib import admin
from .models import Post, Comment, Like
# from .models import PostImage, PostComment
 
# class PostImageAdmin(admin.StackedInline):
#     model = PostImage

# class PostCommentAdmin(admin.StackedInline):
#     model = PostComment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin, PostCommentAdmin]
    
#     class Meta:
#        model = Post
 
# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass

# @admin.register(PostComment)
# class PostCommentAdmin(admin.ModelAdmin):
#     pass
