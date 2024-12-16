from django.db import models
from taggit.managers import TaggableManager

class PostStatusType(models.IntegerChoices):
    active = 1,("فعال")
    disabled = 2,("غیرفعال")
    
class CommentStatusType(models.IntegerChoices):
    active = 1,("فعال")
    disabled = 2,("غیرفعال")

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode = True,unique=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class PostModel(models.Model):
    author = models.ForeignKey("accounts.User",on_delete=models.SET_NULL,null=True)
    slug = models.SlugField(allow_unicode = True,unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to= 'blog/',default= 'blog/blog.jpg')
    category = models.ManyToManyField(PostCategory)
    tags = TaggableManager()
    status = models.IntegerField(choices=PostStatusType.choices,default=PostStatusType.disabled.value)
    counted_view = models.IntegerField(default=0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return " {} - {} ".format(self.id,self.title)
    

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    status = models.IntegerField(choices=CommentStatusType.choices,default=CommentStatusType.disabled.value)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return " {} - {} ".format(self.name,self.email)
    
