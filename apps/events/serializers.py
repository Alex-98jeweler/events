from rest_framework import serializers

from . import models


class BaseEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Event
        fields = '__all__'
        extra_kwargs = {
            "creator": {'read_only': True}
        }

class EventSerializers(BaseEventSerializer):
    pass
    # creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
        