from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Quote(models.Model):
    content = models.TextField(max_length=250, null=False)
    author = models.CharField(max_length= 100)

    class  Meta:
        verbose_name_plural  =  "Quotes"    

    def __str__(self):
        return self.content    