from django.db import models
from django.utils.text import slugify

# Create your models here.

class ContactInfo(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  email = models.CharField(max_length=100, blank=False, null=False, default="")
  phone = models.CharField(max_length=100, blank=False, null=False, default="")
  info = models.CharField(max_length=100, blank=False, null=False, default="")

  def __unicode__(self):
    return self.name

class FocusArea(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")

  def __unicode__(self):
    return self.name

  def get_absolute_url(self):
    return "/areas/%s" % slugify(self.name)

