from rest_framework import serializers
from simulativ.profiles import models


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = models.Profile
        fields = '__all__'


class ProfileAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profile
        fields = ("avatar",)


class ProfileStatusSerializer(serializers.ModelSerializer):

    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.ProfileStatus
        fields = '__all__'




