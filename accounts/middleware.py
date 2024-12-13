from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin
from urllib.parse import urlparse, urlunparse

class HSTSMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.is_secure():
            # Construct absolute URI manually
            url_parts = list(urlparse(request.build_absolute_uri()))
            url_parts[0] = 'https'
            response = HttpResponsePermanentRedirect(urlunparse(url_parts))

            response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
            return response
