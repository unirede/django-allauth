from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import WebmonitorProvider


urlpatterns = default_urlpatterns(WebmonitorProvider)
