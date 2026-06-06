from rest_framework import serializers
from .models import ShortUrl

class ShortUrlSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = "__all__"
        read_only_fields = ["shortcode","clicks"]