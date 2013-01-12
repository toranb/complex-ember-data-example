from codecamp.ember import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
    url(r'^/tags/$', csrf_exempt(views.TagList.as_view())),
    url(r'^/ratings/$', csrf_exempt(views.RatingList.as_view())),
    url(r'^/speakers/$', csrf_exempt(views.SpeakerList.as_view())),
    url(r'^/personas/$', csrf_exempt(views.PersonaList.as_view())),
    url(r'^/companies/$', csrf_exempt(views.CompanyList.as_view())),
    url(r'^/sponsors/$', csrf_exempt(views.SponsorList.as_view())),
    url(r'^/associations/$', csrf_exempt(views.AssociationList.as_view())),
    url(r'^/sessions/$', csrf_exempt(views.SessionList.as_view())),
    url(r'^/tags/(?P<pk>\d+)/$', csrf_exempt(views.TagDetail.as_view())),
    url(r'^/ratings/(?P<pk>\d+)/$', csrf_exempt(views.RatingDetail.as_view())),
    url(r'^/speakers/(?P<pk>\d+)/$', csrf_exempt(views.SpeakerDetail.as_view())),
    url(r'^/personas/(?P<pk>\d+)/$', csrf_exempt(views.PersonaDetail.as_view())),
    url(r'^/companies/(?P<pk>\d+)/$', csrf_exempt(views.CompanyDetail.as_view())),
    url(r'^/sponsors/(?P<pk>\d+)/$', csrf_exempt(views.SponsorDetail.as_view())),
    url(r'^/associations/(?P<pk>\d+)/$', csrf_exempt(views.AssociationDetail.as_view())),
    url(r'^/sessions/(?P<pk>\d+)/$', csrf_exempt(views.SessionDetail.as_view())),
    url(r'^/sessions/(?P<session_pk>\d+)/tags/$', csrf_exempt(views.TagBySessionList.as_view())),
    url(r'^/sessions/(?P<session_pk>\d+)/ratings/$', csrf_exempt(views.RatingBySessionList.as_view())),
    url(r'^/sessions/(?P<session_pk>\d+)/speakers/$', csrf_exempt(views.SpeakerBySessionList.as_view())),
    url(r'^/associations/(?P<association_pk>\d+)/speakers/$', csrf_exempt(views.SpeakerByAssociationList.as_view())),
    url(r'^/speakers/(?P<speaker_pk>\d+)/personas/$', csrf_exempt(views.PersonaBySpeakerList.as_view())),
    url(r'^/companies/(?P<company_pk>\d+)/sponsors/$', csrf_exempt(views.SponsorByCompanyList.as_view())),
)
