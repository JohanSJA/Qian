from django.db import models

class Category(models.Model):
    code = models.CharField(max_length=6, unique=True)
    description = models.CharField(max_length=20, blank=True, unique=True)
    type = models.CharField(max_length=1, choices=[
            ("F", "Finished Goods"),
            ("M", "Raw Materials"),
            ("D", "Dummy Item - (No Movements)"),
            ("L", "Labor")
        ])
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __unicode__(self):
        return self.code
