from django.db import models

# Create your models here.


class AmiiboSeries(models.Model):
    amiibo_series_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) # amiibo series/line name
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'amiibo_series'   # custom table name; I like this better
        verbose_name_plural = "amiibo series"
        
class AmiiboUniverse(models.Model):
    amiibo_universe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) # universe name
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'amiibo_universe'   #custom table name; I like this better
        
class Amiibo(models.Model): # MANY "amiibo characters" to ONE "universe" & MANY "amiibo characters" to ONE "series"
    amiibo_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='amiibo/', null=True, blank=True)   #creates folder called amiibo under the main media folder and uploads there
    name = models.CharField(max_length=200, verbose_name='character') # character name
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    universe = models.ForeignKey(AmiiboUniverse)    
    series = models.ForeignKey(AmiiboSeries)
    #release_date (hard to pin down exact dates for some..)
    #exclusive
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'amiibo'   # custom table name; I like this better
        verbose_name_plural = "amiibo"