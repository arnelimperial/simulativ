from django.test import TestCase
from django.conf import settings
import json
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from simulativ.profiles.api import serializers
from simulativ.profiles import models

User = get_user_model()


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            "username": "testcase",
            "email": "test@test1.io",
            "first_name": "Arnel",
            "last_name": "Imperial",
            "password1": "1234ABcd/",
            "password2": "1234ABcd/",
        }

        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    list_url = reversed("profile-list")

    def setUp(self):
        self.user = User.objects.create_user(
            username="davinci",
            email="test@test.io",
            first_name="Arnel",
            last_name="Imperial",
            password="strong_Password1")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def profile_list_unauthenticated(self):
        self.client.force_authenticate(username=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse("profile-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], "davinci")

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}), {"country": "Philippines"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
            "id": 1,
            "user": "davinci",
            "country": "Philippines",
            "city": "QC",
            "phone_number": "+358401646222",
            "avatar": None
        })

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(
            username="davinci1",
            email="test@test.org",
            first_name="Arnel",
            last_name="Imperial",
            password="strong_Password2")
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}), {"country": "Philippines"})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)






