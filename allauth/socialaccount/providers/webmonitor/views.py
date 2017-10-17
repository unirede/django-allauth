import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import WebmonitorProvider


class WebmonitorOAuth2Adapter(OAuth2Adapter):
    provider_id = WebmonitorProvider.id
    access_token_url = 'https://oauthtst.webmonitor.global/token'
    authorize_url = 'https://oauthtst.webmonitor.global/authorize'
    profile_url = 'https://oauthtst.webmonitor.global/userinfo'

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.profile_url,
                            params={'access_token': token.token,
                                    'alt': 'json'})
        resp.raise_for_status()
        extra_data = resp.json()
        login = self.get_provider() \
            .sociallogin_from_response(request,
                                       extra_data)
        return login


oauth2_login = OAuth2LoginView.adapter_view(WebmonitorOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(WebmonitorOAuth2Adapter)
