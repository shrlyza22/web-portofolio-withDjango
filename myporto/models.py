from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Emoji or Icon for the skill (e.g. 🐍, 🎯)")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Emoji or Icon for the project (e.g. 🛒, 📈)")
    repo_link = models.URLField(blank=True, null=True, help_text="Link GitHub atau Source Code")
    
    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    link = models.URLField()
    date_published = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
