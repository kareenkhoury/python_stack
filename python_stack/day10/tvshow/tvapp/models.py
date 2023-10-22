from django.db import models
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        if len(postData['release_date']) < 10:
            errors["release_date"] = "Show releasedate should be at least 10 characters"
        return errors
class shows(models.Model):
    title = models.TextField()
    network = models.TextField()
    release_date = models.DateField()
    description = models.TextField()
    objects = ShowManager()