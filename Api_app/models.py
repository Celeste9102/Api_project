from django.db import models

# Create your models here.

# orm 建表

class DB_notice(models.Model):
    content = models.CharField(max_length=100,null=True,blank=True,default='')
    def __str__(self):
        return self.content[:3]