from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class PostModel(models.Model):
    author = models.ForeignKey("accounts.User",on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to= 'blog/')
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=False)
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
    status = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return " {} - {} ".format(self.name,self.email)
    
