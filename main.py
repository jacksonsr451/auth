from flask import Flask
from flask_jwt_extended import JWTManager

from interfaces.auth_controller import auth_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'
jwt = JWTManager(app)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
