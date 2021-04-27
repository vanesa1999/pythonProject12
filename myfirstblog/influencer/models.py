from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
from ckeditor.fields import RichTextField

class Author(models.Model):
    user= models.OneToOneField( User, on_delete= models.CASCADE)
    bio= models.TextField(max_length=1000)

    class Meta:
        ordering= ['user']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.bio}'

class Blog (models.Model):
    title= models.CharField(max_length=200, help_text= 'Enter the name of the blog')
    author= models.ForeignKey( User , on_delete=models.CASCADE)
    post_date= models.DateTimeField(help_text='Post Date',auto_now_add=True , editable=False, blank=True)
    content= RichTextField(blank= True, null= True)
    likes= models.ManyToManyField(User, related_name='blog_p', blank=True, null= True)

    class Meta:
        ordering= ['-post_date']
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url (self):
        return reverse('blog-detail', args= [str(self.id)])

class Comment (models.Model):
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
    text= models.CharField(max_length=300, help_text='Enter a comment')
    comment_date= models.DateTimeField(help_text='Comment Date')
    userc= models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta:
        ordering= ['-comment_date']

    def __str__(self):
        return self.text


