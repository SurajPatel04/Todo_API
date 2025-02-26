from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.TextField(blank=False, null=False)
    lastDate = models.DateField()  # user write date here
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

class subtodo(models.Model):
    subTitle = models.TextField(blank = True, null=True)
    subLastDat = models.DateField() # user write date here
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subTitle
