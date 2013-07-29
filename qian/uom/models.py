from django.db import models

class UOM(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Unit of Measure"
        verbose_name_plural = "Units of Measure"
    
    def __unicode__(self):
        return self.name
