from rest_framework import serializers
from . import models

class DocumentSerializer(serializers.ModelSerializer):
   class Meta:
      model = models.Document
      fields = ('id', 'title', 'description', 'file_url', 'image_url', 'updated_at', 'company')


class CompanySerializer(serializers.ModelSerializer):
   class Meta:
      model = models.Company
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
      )
