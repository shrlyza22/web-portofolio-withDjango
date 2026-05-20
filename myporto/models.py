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
    
    def __str__(self):
        return self.title
