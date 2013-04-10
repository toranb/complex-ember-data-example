from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    description = models.CharField(max_length=200)

class Session(models.Model):
    name = models.CharField(max_length=150)
    room = models.CharField(max_length=100)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    tags = models.ManyToManyField(Tag)

class Association(models.Model):
    name = models.CharField(max_length=150)

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    web = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    bio = models.TextField()
    session = models.ForeignKey(Session, blank=True, null=True, related_name='speakers')
    association = models.ForeignKey(Association, blank=True, null=True, related_name='speakers')
    zidentity = models.ForeignKey(User, blank=True, null=True, related_name='aliases')

class Rating(models.Model):
    score = models.IntegerField()
    feedback = models.CharField(max_length=140)
    session = models.ForeignKey(Session, related_name='ratings')

class Company(models.Model):
    name = models.CharField(max_length=100)

class Persona(models.Model):
    nickname = models.CharField(max_length=100)
    company = models.ForeignKey(Company)
    speaker = models.ForeignKey(Speaker, related_name='personas')

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, related_name='sponsors')
