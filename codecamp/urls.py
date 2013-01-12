from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from codecamp.ember.views import HomeView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^codecamp', include('codecamp.ember.urls', namespace='codecamp')),
    url(r'^$', HomeView.as_view()),
)
