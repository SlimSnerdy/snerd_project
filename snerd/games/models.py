from django.db import models

# Create your models here.


# class GameCompanyRole(models.Model):
    # role_id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=200)
    
    # def __unicode__(self):
        # return self.name
    
    # class Meta:
        # db_table = 'game_company_role'
        
class GamePlatform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        db_table = 'game_platform'        
        
class GameCompany(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
#   role = models.ManyToManyField(GameCompanyRole, db_table='game_company_to_role')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'game_company'
        verbose_name_plural = "Game companies"
        
class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    release_date = models.DateField(null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    company = models.ManyToManyField(GameCompany, db_table='game_to_company')
    platform = models.ManyToManyField(GamePlatform, db_table='game_to_platform')
    
    def __unicode__(self):
        return self.title
    
    def get_gamecompany(self):
        return " / ".join([n.name for n in self.company.all()])
    get_gamecompany.short_description = 'Company'
    
    def get_gameplatform(self):
        return " / ".join([n.name for n in self.platform.all()])
    get_gameplatform.short_description = 'Platform'
    
    class Meta:
        db_table = 'game'   # custom table name; I like this better