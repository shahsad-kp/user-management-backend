from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.ReadOnlyField(source='is_superuser')
    profilePicture = serializers.SerializerMethodField(source='profile_picture')

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'profilePicture', 'isAdmin']
        extra_kwargs = {
            'username': {'read_only': True},
            'name': {'read_only': True},
        }

    def get_profilePicture(self, user):
        if user.profile_picture:
            return user.profile_picture.url
        else:
            return None

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        profile_picture = validated_data.pop('profilePicture', None)
        user = User.objects.create_user(**validated_data)

        if profile_picture:
            user.profile_picture = profile_picture
            user.save()

        if password:
            user.set_password(password)
            user.save()

        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', None)
        data['profilePicture'] = data.pop('profilePicture', None)
        return data

