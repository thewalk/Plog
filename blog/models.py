from django.db import models

# Create your models here.

class Tag(models.Model):
    """Tag, each article at least has a tag as an abstraction"""
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.tag_name)

class Category(models.Model):
    """Category, each article is belong to some category"""
    category_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%s' %(self.category_name)

class Article(models.Model):
    """Article"""
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    hit_num = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % (self.title, self.publish_time)
        
class Comment(models.Model):
    """Comment, comment of article"""
    critic_name = models.CharField(max_length=20)
    article = models.ForeignKey(Article)
    email = models.EmailField(blank=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.critic_name)
