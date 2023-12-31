from rest_framework import serializers

from . import services


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    birthday = serializers.DateField()

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data)
    
    class Meta:
        extra_kwargs = {
            'birthday': {"required": False}
        }
        ref_name = 'User 2'