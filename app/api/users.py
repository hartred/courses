from app.api.service.user import UserService
from app.api.serializers.user import UserSchema

from flask import request

from flask_classy import FlaskView

from flask_apispec.annotations import marshal_with, doc


@marshal_with(UserSchema)
class UserView(FlaskView):

    @marshal_with(UserSchema(many=True))
    @doc(description='Get List of all users')
    def index(self):
        """List of users"""
        return UserService.list()

    @marshal_with(UserSchema)
    def get(self, id):
        """Retrieve one user"""
        return UserService.one(id)

    @doc(description='Updates user')
    @marshal_with(UserSchema)
    def patch(self, id):
        """Update user"""
        data = request.get_json()
        return UserService.update(data, id)

    @doc(description='Deletes user')
    def delete(self, id):
        """Delete User"""
        return UserService.delete(id)



