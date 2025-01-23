import django
from django.utils import translation
from django.conf import settings
from typing import Optional
from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin


class UserLanguageMiddleware(MiddlewareMixin):
    """
    Middleware that sets the language for authenticated users based on their user.language preference.
    Compatible with Django 3.2+
    """
    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        user = getattr(request, 'user', None)
        if not user:
            return response

        if not user.is_authenticated:
            return response

        user_language = getattr(user, 'language', None)
        if not user_language:
            return response

        current_language = translation.get_language()
        if user_language == current_language:
            return response

        translation.activate(user_language)
        request.session[settings.LANGUAGE_CODE] = user_language

        return response
