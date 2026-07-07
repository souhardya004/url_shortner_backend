from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortUrl
from .serializers import ShortUrlSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from .utils import make_short_code

# Create your views here.

class ShortUrlViewset(viewsets.ModelViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializers

    def perform_create(self, serializer):

        short_code = make_short_code()
        while ShortUrl.objects.filter(shortcode=short_code).exists():
            short_code = make_short_code()

        serializer.save(shortcode=short_code)

def redirect_short_url(request, shortcode):
    url = get_object_or_404(ShortUrl, shortcode=shortcode)
    url.clicks += 1
    url.save()
    return redirect(url.original_url)