from flask import Flask, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity
from models import db, User, Recipe

app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipe_manager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a strong secret key

# Initialize the database
db.init_app(app)

# JWT (JSON Web Tokens) setup
jwt = JWT(app, lambda username, password: User.query.filter_by(username=username, password=password).first())

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Both username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return jsonify({'access_token': jwt.jwt_encode_callback(user)}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

# Recipe management endpoints (you can expand these)
@app.route('/recipes', methods=['POST'])
@jwt_required()
def create_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        name=data['name'],
        ingredients=data['ingredients'],
        preparation=data['preparation'],
        cooking_time=data['cooking_time'],
        user_id=current_identity.id
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe created successfully'}), 201

@app.route('/recipes', methods=['GET'])
@jwt_required()
def get_recipes():
    user_id = current_identity.id
    recipes = Recipe.query.filter_by(user_id=user_id).all()
    return jsonify([recipe.serialize() for recipe in recipes])

# ... (similarly, implement GET, PUT, and DELETE routes for individual recipes)

if __name__ == '__main__':
    app.run(debug=True)
