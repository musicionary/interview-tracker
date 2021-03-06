from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class DocumentSerializer(serializers.ModelSerializer):
   class Meta:
      model = models.Document
      fields = ('id', 'title', 'description', 'file_url', 'image_url', 'updated_at', 'company')


class CompanySerializer(serializers.ModelSerializer):
   documents = serializers.PrimaryKeyRelatedField(
      many=True,
      read_only=True)

   class Meta:
      model = models.Company
      owner = serializers.ReadOnlyField(source='owner.username')
      fields = (
         'id',
         'name',
         'main_contact',
         'main_contact_email',
         'street',
         'city',
         'state',
         'zip',
         'phone',
         'company_email',
         'company_website',
         'posting_link',
         'position',
         'response_date',
         'outcome',
         'discovery_date',
         'application_sent',
         'interview_scheduled',
         'interview_location',
         'interview_date',
         'follow_up_date',
         'thank_you_note_sent',
         'notes',
         'follow_up_steps',
         'created_at',
         'updated_at',
         'owner',
         'documents',
      )


class UserSerializer(serializers.ModelSerializer):
   companies = serializers.PrimaryKeyRelatedField(
      many=True,
      read_only=True)

   class Meta:
      model = User
      fields = ('id', 'username', 'companies',)
