from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

User = getattr(settings, 'AUTH_USER_MODEL')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=70, blank=True)
    #address1 = models.TextField(blank=True)
    #address2 = models.TextField(blank=True)
    #state = models.CharField(max_length=70, blank=True)
    #region = models.CharField(max_length=70, blank=True)
    #province = models.CharField(max_length=70, blank=True)
    #postal_code = models.CharField(max_length=10, blank=True)
    phone_number = PhoneNumberField(blank=True)
    avatar = models.ImageField(blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.user.email


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'statuses'

    def __str__(self):
        return str(self.user_profile)



