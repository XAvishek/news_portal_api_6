from rest_framework import serializers
from apis.accounts.models import Profile, User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "dob", "address"
        # fields = "__all__"
        # extra_kwargs = {
        #     "address": {"required": False}
        # }

class UserCreateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name", "role", "profile")

    def create(self, validate_data):
        profile = validate_data.pop("profile")
        raw_password = validate_data.pop("password")

        user = User(**validate_data)
        user.set_password(raw_password)
        user.save()

        Profile.objects.create(**profile, user=user)
        return user

    