from django.views.generic import TemplateView
from codecamp.ember import serializers
from rest_framework import generics
from codecamp.ember.models import Session, Speaker, Rating, Tag, Association, Sponsor, Persona, Company

class HomeView(TemplateView):
    template_name = 'index.html'

class AssociationList(generics.ListCreateAPIView):
    model = Association
    serializer_class = serializers.AssociationSerializer

class AssociationDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Association
    serializer_class = serializers.AssociationSerializer

class SessionList(generics.ListCreateAPIView):
    model = Session
    serializer_class = serializers.SessionSerializer

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Session
    serializer_class = serializers.SessionSerializer

class TagBySessionList(generics.ListCreateAPIView):
    model = Tag
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        session_pk = self.kwargs.get('session_pk', None)
        if session_pk is not None:
            return Tag.objects.filter(session__pk=session_pk)
        return []

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Tag
    serializer_class = serializers.TagSerializer

class SpeakerBySessionList(generics.ListCreateAPIView):
    model = Speaker
    serializer_class = serializers.SpeakerSerializer

    def get_queryset(self):
        session_pk = self.kwargs.get('session_pk', None)
        if session_pk is not None:
            return Speaker.objects.filter(session__pk=session_pk)
        return []

class SpeakerByAssociationList(generics.ListCreateAPIView):
    model = Speaker
    serializer_class = serializers.SpeakerSerializer

    def get_queryset(self):
        association_pk = self.kwargs.get('association_pk', None)
        if association_pk is not None:
            return Speaker.objects.filter(association__pk=association_pk)
        return []

class SpeakerDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Speaker
    serializer_class = serializers.SpeakerSerializer

class RatingBySessionList(generics.ListCreateAPIView):
    model = Rating
    serializer_class = serializers.RatingSerializer

    def get_queryset(self):
        session_pk = self.kwargs.get('session_pk', None)
        if session_pk is not None:
            return Rating.objects.filter(session__pk=session_pk)
        return []

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Rating
    serializer_class = serializers.RatingSerializer

class SponsorByCompanyList(generics.ListCreateAPIView):
    model = Sponsor
    serializer_class = serializers.SponsorSerializer

    def get_queryset(self):
        company_pk = self.kwargs.get('company_pk', None)
        if company_pk is not None:
            return Sponsor.objects.filter(company__pk=company_pk)
        return []

class PersonaBySpeakerList(generics.ListCreateAPIView):
    model = Persona
    serializer_class = serializers.PersonaSerializer

    def get_queryset(self):
        speaker_pk = self.kwargs.get('speaker_pk', None)
        if speaker_pk is not None:
            return Persona.objects.filter(speaker__pk=speaker_pk)
        return []

class PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Persona
    serializer_class = serializers.PersonaSerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Company
    serializer_class = serializers.CompanySerializer

class SponsorDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Sponsor
    serializer_class = serializers.SponsorSerializer

class TagList(generics.ListCreateAPIView):
    model = Tag
    serializer_class = serializers.TagSerializer

class RatingList(generics.ListCreateAPIView):
    model = Rating
    serializer_class = serializers.RatingSerializer

class SpeakerList(generics.ListCreateAPIView):
    model = Speaker
    serializer_class = serializers.SpeakerSerializer
    filter_fields = ['name']

class PersonaList(generics.ListCreateAPIView):
    model = Persona
    serializer_class = serializers.PersonaSerializer

class CompanyList(generics.ListCreateAPIView):
    model = Company
    serializer_class = serializers.CompanySerializer

class SponsorList(generics.ListCreateAPIView):
    model = Sponsor
    serializer_class = serializers.SponsorSerializer
