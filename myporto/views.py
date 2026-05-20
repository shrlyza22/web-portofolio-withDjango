from django.shortcuts import render
from .models import Skill, Project, Article

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    articles = Article.objects.all()
    return render(request, 'index.html', {'skills': skills, 'projects': projects, 'articles': articles})