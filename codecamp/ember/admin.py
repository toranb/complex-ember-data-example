from django.contrib import admin
from codecamp.ember.models import Session, Speaker, Rating, Tag, Association, Sponsor, Persona, Company

admin.site.register(Tag)
admin.site.register(Session)
admin.site.register(Speaker)
admin.site.register(Rating)
admin.site.register(Association)
admin.site.register(Sponsor)
admin.site.register(Persona)
admin.site.register(Company)
