from django.db import models

# Create your models here.

        
class IceCreamBrand(models.Model):
    ice_cream_brand_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
#    rating = models.DecimalField(max_digits=3, decimal_places=1)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'ice_cream_brand'   # custom table name; I like this better
        
class IceCream(models.Model): # MANY "ice cream flavors" to ONE "ice cream brand"
    ice_cream_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='flavor') # flavor name
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    brand = models.ForeignKey(IceCreamBrand)    
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'ice_cream'   # custom table name; I like this better