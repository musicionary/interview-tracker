import datetime
from django.db import models
from django.utils import timezone

class Document(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField(blank=True, default='')
    file_url = models.TextField(blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.TextField(blank=False, default='')

    company = models.ForeignKey(
        'Company',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="documents",
        related_query_name="document"
    )

    def __str__(self):
        return self.title

    def was_updated_recently(self):
        return self.updated_at >= timezone.now() - datetime.timedelta(days=1)

class Company(models.Model):
    name = models.CharField(max_length=60, blank=False, default='')
    main_contact = models.CharField(max_length=60, blank=True)
    main_contact_email = models.EmailField(blank=True)
    street = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=40, blank=True)
    state = models.CharField(max_length=20, blank=True)
    zip = models.CharField(max_length=11, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    company_email = models.EmailField(blank=False, default='')
    company_website = models.CharField(max_length=60, blank=False, default='')

    posting_link = models.CharField(max_length=60, blank=False, default='')
    position = models.CharField(max_length=60, blank=False, default='')
    response_date = models.DateField()
    outcome = models.CharField(max_length=60, blank=False, default='')

    discovery_date = models.DateField()
    application_sent = models.BooleanField(default=False)
    interview_scheduled = models.BooleanField(default=False)
    interview_location = models.CharField(max_length=250, blank=True)
    interview_date = models.DateTimeField()
    follow_up_date = models.DateField()
    thank_you_note_sent = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    follow_up_steps = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
