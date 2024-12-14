from flask import Blueprint, jsonify, request
from . import db
from .models import App

bp = Blueprint('routes', __name__)  

@bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the App Management API",
        "endpoints": {
            "GET /": "Home page",
            "GET /apps": "List all apps",
            "POST /add-app": "Create a new app",
            "GET /get-app/<id>": "Get app details",
            "DELETE /apps/<id>": "Delete an app"
        }
    })

@bp.route("/apps", methods=["GET"])
def get_apps():
    apps = App.query.all()
    apps_list = []
    for app in apps:
        apps_list.append({
            "id": app.id,
            "app_name": app.app_name,
            "version": app.version,
            "description": app.description
        })
    return jsonify(apps_list)

@bp.route("/add_app", methods=["POST"])
def add_app():
    app_name = request.form.get("app_name")
    version = request.form.get("version")
    description = request.form.get("description")

    if not app_name or not version or not description:
        return jsonify({"error": "All fields are required."}), 400

    new_app = App(app_name=app_name, version=version, description=description)
    db.session.add(new_app)
    db.session.commit()

    return jsonify({"message": "App added successfully", "id": new_app.id}), 201

@bp.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app = App.query.get(id)

    if not app:
        return jsonify({"error": "App not found"}), 404

    return jsonify({
        "id": app.id,
        "app_name": app.app_name,
        "version": app.version,
        "description": app.description
    })

@bp.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    app = App.query.get(id)

    if not app:
        return jsonify({"error": "App not found"}), 404

    db.session.delete(app)
    db.session.commit()

    return jsonify({"message": "App deleted successfully"})
