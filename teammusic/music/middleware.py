from django.shortcuts import redirect
from django.conf import settings

class CognitoLoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ตรวจสอบว่าโทเค็นล็อกอินอยู่ใน session หรือไม่
        if not request.session.get('access_token'):
            if request.path not in [settings.LOGIN_URL, '/teammusic/signup/', '/teammusic/confirm/', '/teammusic/']:
                return redirect(settings.LOGIN_URL)
        response = self.get_response(request)
        return response
