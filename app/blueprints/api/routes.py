from .import bp as api
from flask import jsonify, request
from app import db
from app.blueprints.auth.models import Character, User

# I think i did this right. If not, oh well. 
# CREATE MARVEL CHARACTER


@api.route('/character', methods=['POST'])
@token_required
def create_character(current_user_token):
    name = request.json['name']
    description = request.json['description']
    super_power = request.json['super_power']
    comics_appeared_in = request.json['comics_appeared_in']
    user_token = current_user_token.token

    character = Character(name, description, super_power, comics_appeared_in,user_token=user_token)

    db.session.add(character)
    db.session.commit()

    return jsonify(response)

# RETRIEVE ALL MARVEL CHARACTERS


@api.route('/character', methods=['GET'])
@token_required
def get_character(current_user_token):
    owner = current_user_token.token
    character = Character.query.filter_by(user_token=owner).all()
    return jsonify(response)


# UPDATE MARVEL CHARACTER


@api.route('/character/<id>', methods=['POST', 'PUT'])
@token_required
def update_character(current_user_token, id):
    character = Character.query.get(id)

    character.name = request.json['name']
    character.description = request.json['description']
    character.super_power = request.json['super_power']
    character.comics_appeared_in = request.json['comics_appeared_in']
    character.user_token = current_user_token.token

    db.session.commit()


# DELETE MARVEL CHARACTER


@api.route('/character/<id>', methods=['DELETE'])
@token_required
def delete_character(current_user_token, id):
    db.session.delete(Character)
    db.session.commit()
