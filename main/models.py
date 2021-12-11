from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class quoteCategory(models.Model):
    category = CharField.model(max_length=100)

    def __str__(self):
        return self.category
    
    class  Meta:
        verbose_name_plural  =  "Categories"

class Quote(models.Model):
    content = TextField.model(max_length=250, null=False)
    category = models.ForeignKey(quoteCategory, verbose_name="category", on_delete=models.CASCADE)
    author = CharField.model(max_length= 100)

    def __str__(self):
        return self.id

    class  Meta:
        verbose_name_plural  =  "Quotes"    