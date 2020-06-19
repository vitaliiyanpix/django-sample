from django.contrib.auth import get_user_model
from rest_framework import serializers


USER_ROLE_CHOICES = (
    ('provider', 'provider'),
    ('customer', 'customer'),
)


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(max_length=128, write_only=True, )

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name', 'password', 'password_confirm', 'role']
        extra_kwargs = {
            'password':  {'write_only': True},
            'role':  {'choices': USER_ROLE_CHOICES}
        }

    def validate_confirm_password(self, confirm_password):
        request = self.context.get('request')
        password = request.data.get('password')
        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError('Password mismatch')
        return confirm_password

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password_confirm')
        user = self.Meta.model.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
