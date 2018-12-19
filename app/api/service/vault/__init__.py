from app.api.decorators.token import token_required
from app.api.serializers.vault import VaultSchema
from app.models.models import Vault
from app.shortcuts import dbsession

from flask import jsonify


class VaultService:

    @staticmethod
    @token_required
    def list(current_user, id):

        if not current_user.id == int(id):
            return jsonify({'message': 'permission denied'})

        vaults = Vault.query.filter_by(owner_id=current_user.id)

        schema = VaultSchema(many=True)
        output = schema.dump(vaults).data

        return jsonify({'vaults': output})

    @staticmethod
    @token_required
    def one(current_user, id):

        vault = Vault.query.filter_by(vault_id=id).first()

        if vault not in current_user.vaults:
            return jsonify({'message': 'permission denied'})

        if not vault:
            return jsonify({"message": 'no vault'})

        schema = VaultSchema()

        output = schema.dump(vault).data

        return jsonify({'vault': output})

    @staticmethod
    @token_required
    def create(current_user, id, data):

        if not current_user.id == int(id):
            return jsonify({'message': 'permission denied'})

        if not data:
            return jsonify({'message': 'empty'})

        new_vault = Vault(description=data['description'],
                          title=data['title'],
                          owner_id=current_user.id)

        dbsession.add(new_vault)
        dbsession.commit()

        return jsonify({'message': 'vault created'})

    @staticmethod
    @token_required
    def update(data, current_user, id):

        vault = Vault.query.filter_by(id=id).first()

        if vault not in current_user.vaults:
            return jsonify({'message': 'permission denied'})

        if 'description' in data:
            vault.description = data['description']

        if 'title' in data:
            vault.title = data['title']

        dbsession.commit()

        return jsonify({'message': 'vault updated'})

    @staticmethod
    @token_required
    def delete(current_user, id):

        vault = Vault.query.filter_by(vault_id=id).first()
        if vault not in current_user.vaults:
            return jsonify({'message': 'permission denied'})

        dbsession.delete(vault)
        dbsession.commit()

        return jsonify({'message': 'vault has been deleted'})
