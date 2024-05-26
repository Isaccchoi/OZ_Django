from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers


User = get_user_model()


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        user = User(**data)

        try:
            validate_password(password=data['password'], user=user)
        except ValidationError as e:
            raise serializers.ValidationError(list(e.messages))

        return super().validate(data)

    def create(self, validated_data):
        user = User(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user
