from django.db import models
from django.utils.text import slugify
from django.conf import settings

# Create your models here.

class ActivityMap(models.Model):
  image = models.ImageField(upload_to='activity_maps/', default="")
  is_default = models.BooleanField(default=False)

class Project(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  info = models.CharField(max_length=255, blank=False, null=False, default="")

  def __unicode__(self):
    return self.name

  def get_absolute_url(self):
    return "/projects#p-%s" % self.pk

class ProjectAsset(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  image = models.CharField(max_length=255, blank=True, null=True, default="", editable=False)
  full_res_image = models.ImageField(upload_to='project_assets/', default="")
  is_default = models.BooleanField(default=False)
  project = models.ForeignKey('Project')

  def __unicode__(self):
    return self.name

  def save(self):
    super(ProjectAsset, self).save()
    import Image
    path = self.full_res_image.path
    image = Image.open(path)
    r = float(image.size[1])/float(image.size[0])
    image = image.resize((900, int(900*r)))
    path = path.split(".")
    path = "%s-small.%s" % (path[0], path[1])
    image.save(path)
    path = path.split(settings.MEDIA_URL)
    self.image = "%s" % (path[1])
    super(ProjectAsset, self).save()
  

class ContactInfo(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default="")
  email = models.CharField(max_length=100, blank=False, null=False, default="")
  cell = models.CharField(max_length=100, blank=False, null=False, default="")
  office = models.CharField(max_length=100, blank=True, null=True, default="")
  info = models.CharField(max_length=100, blank=False, null=False, default="")

  def __unicode__(self):
    return self.name

  def emailHTML(self):
    if not self.email:
      return ""
    html = "<a href='mailto:%s'>%s</a>" % (self.email, self.email)
    return html

  def officeHTML(self):
    import re
    if not self.office:
      return ""
    phone = re.sub(r'[().-]+',"", self.office)
    phone = "(%s)%s-%s" % (phone[0:3], phone[3:6], phone[6:])
    return "<a href='callto:%s'>%s</a>" % (self.office, phone)

  def cellHTML(self):
    import re
    if not self.cell:
      return ""
    phone = re.sub(r'[().-]+',"", self.cell)
    phone = "(%s)%s-%s" % (phone[0:3], phone[3:6], phone[6:])
    return "<a href='callto:%s'>%s</a>" % (self.cell, phone)

