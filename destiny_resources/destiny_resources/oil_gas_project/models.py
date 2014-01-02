from django.db import models
from django.utils.text import slugify

# Create your models here.

class ActivityMap(models.Model):
  image = models.CharField(max_length=255, blank=False, null=False, default="")
  is_default = models.BooleanField(default=False)

class Project(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  info = models.CharField(max_length=255, blank=False, null=False, default="")

  def __unicode__(self):
    return self.name

class ProjectAsset(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  image = models.CharField(max_length=255, blank=False, null=False, default="")
  full_res_image = models.CharField(max_length=255, blank=False, null=False, default="")
  is_default = models.BooleanField(default=False)
  project = models.ForeignKey('Project')

  def __unicode__(self):
    return self.name

class ContactInfo(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  email = models.CharField(max_length=100, blank=False, null=False, default="")
  phone = models.CharField(max_length=100, blank=False, null=False, default="")
  info = models.CharField(max_length=100, blank=False, null=False, default="")

  def __unicode__(self):
    return self.name

  def emailHTML(self):
    if not self.email:
      return ""
    html = "<a href='mailto:%s'>%s</a>" % (self.email, self.email)
    return html

  def phoneHTML(self):
    import re
    if not self.phone:
      return ""
    phone = re.sub(r'[().-]+',"", self.phone)
    phone = "(%s)%s-%s" % (phone[0:3], phone[3:6], phone[6:])
    html = "<a href='callto:%s'>%s</a>" % (self.phone, phone)
    return html

class FocusArea(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")

  def __unicode__(self):
    return self.name

  def get_absolute_url(self):
    return "/areas/%s" % slugify(self.name)

