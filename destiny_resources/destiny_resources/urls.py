from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'destiny_resources.views.home', name='home'),
     url(r'^contact$', 'destiny_resources.views.contact', name='contact'),
     url(r'^about$', 'destiny_resources.views.about', name='about'),
     url(r'^business-plan$', 'destiny_resources.views.business_plan', name='business_plan'),
     url(r'^projects/(?P<slug>.*)$', 'destiny_resources.views.project', name='project'),
     url(r'^projects$', 'destiny_resources.views.projects', name='projects'),
    # url(r'^destiny_resources/', include('destiny_resources.foo.urls')),

     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
)
