from django.db import models
class PersonalInformation(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skill1 = models.CharField(max_length=100)
    skill2 = models.CharField(max_length=100)
    skill3 = models.CharField(max_length=100)
    skill4 = models.CharField(max_length=100)
    skill5 = models.CharField(max_length=100)

class Education(models.Model):
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

class Language(models.Model):
    language = models.CharField(max_length=100)

class Project(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()

class Experience(models.Model):
    company = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()

class Achievement(models.Model):
    first = models.CharField(max_length=100)
    second = models.CharField(max_length=100)