from django.db import models

class Airports(models.Model):
    airport_code = models.CharField(max_length=255,unique=True)
    position  = models.CharField(max_length=20)
    duration  = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    master_airport = models.CharField(max_length=255,null=True,blank=True)
    parent_port = models.CharField(max_length=255,null=True,blank=True)
    

    class Meta:
        db_table = 'airports_tbl'
        verbose_name = 'Airport'
        verbose_name_plural = 'Airports'
        ordering = ['-created_at']
        indexes = [
        
            models.Index(fields=['airport_code']),             #  Useful if you filter by status
            models.Index(fields=['position', 'duration']), #  Composite index (e.g. for dashboard sorting)
        ]
    
    def __str__(self):
        return self.airport_code 
   
    

    # airport_code = 'B'
    # position  = "left"
    # duration  = 250
    # is_active = True
    # created_at = 
    # master_airport = 'A'
    # parent_port = 'A'

    # airport_code = 'C'
    # position  = "right"
    # duration  = 100
    # is_active = True
    # created_at = 
    # master_airport = 'A'
    # parent_port = 'A'

    # airport_code = 'D'
    # position  = "left"
    # duration  = 50
    # is_active = True
    # created_at = 
    # master_airport = 'A'
    # parent_port = 'B'


    