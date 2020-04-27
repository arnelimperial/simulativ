from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# from django_address.models import AddressModel
from . import managers


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    # name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(_("First Name"), max_length=100)
    last_name = CharField(_("Last Name"), max_length=100)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    objects = managers.UserManager()

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
