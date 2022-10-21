from msilib.schema import Media
from rest_framework import serializers
from upload.models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
