from django.db import models

class MyInfo(models.Model):
    slackUsername = models.CharField(max_length=200)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField()
    
    def __str__(self):
        return self.slackUsername + ' ' + '(' + self.bio + ')'  