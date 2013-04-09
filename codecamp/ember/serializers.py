from rest_framework import serializers
from codecamp.ember.models import Session, Speaker, Rating, Tag, Association, Sponsor, Persona, Company, User

class AssociationSerializer(serializers.ModelSerializer):
    speakers = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = Association
        fields = ('id', 'name', 'speakers')

class SessionSerializer(serializers.ModelSerializer):
    speakers = serializers.ManyPrimaryKeyRelatedField()
    ratings = serializers.ManyPrimaryKeyRelatedField()
    tags = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = Session
        fields = ('id', 'name', 'room', 'desc', 'speakers', 'ratings', 'tags')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'description')

class SpeakerSerializer(serializers.ModelSerializer):
    personas = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = Speaker
        fields = ('id', 'name', 'location', 'session', 'association', 'personas', 'zidentity')

class UserSerializer(serializers.ModelSerializer):
    aliases = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = User
        fields = ('id', 'aliases')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'score', 'feedback', 'session')

class CompanySerializer(serializers.ModelSerializer):
    sponsors = serializers.ManyPrimaryKeyRelatedField()
    class Meta:
        model = Company
        fields = ('id', 'name', 'sponsors')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'nickname', 'speaker', 'company')

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'name', 'company')
