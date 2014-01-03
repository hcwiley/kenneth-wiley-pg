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
    self.image = "%s%s" % (settings.MEDIA_URL, path[1])
    super(ProjectAsset, self).save()
  

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

