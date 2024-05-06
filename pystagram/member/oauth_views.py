from urllib.parse import urlencode

import requests
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.core import signing
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import RedirectView

from member.forms import NicknameForm

User = get_user_model()

NAVER_CALLBACK_URL = '/oauth/naver/callback/'
NAVER_STATE = 'naver_login'
NAVER_LOGIN_URL = 'https://nid.naver.com/oauth2.0/authorize'
NAVER_TOKEN_URL = 'https://nid.naver.com/oauth2.0/token'
NAVER_PROFILE_URL = 'https://openapi.naver.com/v1/nid/me'


class NaverLoginRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        domain = self.request.scheme + '://' + self.request.META.get('HTTP_HOST', '')

        callback_url = domain + NAVER_CALLBACK_URL
        state = signing.dumps(NAVER_STATE)

        params = {
            'response_type': 'code',
            'client_id': settings.NAVER_CLIENT_ID,
            'redirect_uri': callback_url,
            'state': state
        }

        return f'{NAVER_LOGIN_URL}?{urlencode(params)}'


def naver_callback(request):
    code = request.GET.get('code')
    state = request.GET.get('state')

    if NAVER_STATE != signing.loads(state):
        raise Http404

    params = {
        'grant_type': 'authorization_code',
        'client_id': settings.NAVER_CLIENT_ID,
        'client_secret': settings.NAVER_SECRET,
        'code': code,
        'state': state
    }

    response = requests.get(NAVER_TOKEN_URL, params=params)
    result = response.json()
    access_token = result.get('access_token')

    print('token request', result)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(NAVER_PROFILE_URL, headers=headers)

    if response.status_code != 200:
        raise Http404

    result = response.json()
    print('profile request', result)
    email = result.get('response').get('email')

    user = User.objects.filter(email=email).first()

    if user:
        if not user.is_active:
            user.is_active = True
            user.save()

        login(request, user)
        return redirect('main')
