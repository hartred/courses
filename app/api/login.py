from app.api.service.auth import AuthService

from flask import request

from flask_apispec.annotations import doc

from flask_classy import FlaskView


class LoginView(FlaskView):

    @doc(description='Login')
    def post(self):
        data = request.get_json()
        return AuthService.login(data)


