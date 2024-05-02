from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.ManyToManyField(Skill)
    image = models.ImageField(upload_to='project_images/')
    demo_link = models.URLField()
    source_link = models.URLField()

    def __str__(self):
        return self.title
