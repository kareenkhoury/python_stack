from django.db import models
    
class dojo(models.Model):
  state = models.TextField()
  name = models.TextField()
  city = models.TextField()

  
class ninja(models.Model):
    dojo_id = models.ForeignKey(dojo, related_name="dojon", on_delete = models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()