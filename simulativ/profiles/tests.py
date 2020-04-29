from django.test import TestCase
from simulativ.users.models import User
import json
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from simulativ.profiles.api.serializers import ProfileSerializer
from simulativ.profiles.models import Profile, ProfileStatus


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
    list_url = reverse_lazy("profile-list")

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

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_profile_detail_retrieve(self):
    #     response = self.client.get(reverse_lazy("profile-detail", kwargs={"pk": 1}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data["user"], "davinci")

    # def test_profile_update_by_owner(self):
    #     response = self.client.put(reverse_lazy("profile-detail", kwargs={"pk": 1}), {"city": "Makati"})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

        # self.assertEqual(json.loads(response.content), {
        #     "id": 1,
        #     "user": "davinci",
        #     "country": "Philippines",
        #     "city": "QC"
        # })

    # def test_profile_update_by_random_user(self):
    #     random_user = User.objects.create_user(
    #         username="davinci1",
    #         email="test@test.org",
    #         first_name="Arnel",
    #         last_name="Imperial",
    #         password="strong_Password2"
    #     )
    #     self.client.force_authenticate(user=random_user)
    #     response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}), {"country": "Philippines"})
    #
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ProfileStatusViewSetTestCase(APITestCase):
    list_url = reverse("status-list")

    def setUp(self):
        self.user = User.objects.create_user(
            username="davinci",
            email="test@test.io",
            first_name="Arnel",
            last_name="Imperial",
            password="strong_Password1")
        self.status = ProfileStatus.objects.create(user_profile=self.user.profile, status_content='Status test')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_status_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_status_create(self):
        data = {"status_content": "New Status!"}
        response = self.client.post(self.list_url)
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user_profile"], "davinci")
        self.assertEqual(response.data["status_content"], "New Status!")







