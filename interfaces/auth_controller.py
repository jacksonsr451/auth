from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired

from adapters.user_repository_impl import UserRepositoryImpl
from core.use_cases.auth_use_cases import AuthUseCases

auth_bp = Blueprint('auth', __name__)

user_repository = UserRepositoryImpl()
auth_use_cases = AuthUseCases(user_repository)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


@auth_bp.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if auth_use_cases.login(username, password):
            access_token = create_access_token(identity=username)
            return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid username or password'}), 401


@auth_bp.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if auth_use_cases.register(username, password):
            return jsonify({'message': 'Registration successful'}), 200
    return (
        jsonify({'message': 'Invalid username or username already exists'}),
        400,
    )


@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = request.jwt_identity
    return (
        jsonify(
            {'message': f'Hello, {current_user}! This is a protected route.'}
        ),
        200,
    )
