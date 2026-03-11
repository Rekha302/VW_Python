
from flask import Flask
from extensions import db, migrate
from routes.auth_routes import auth_bp
from routes.employee_routes import employee_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/employee_portal"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "secret123"

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(employee_bp)

if __name__ == "__main__":
    app.run(debug=True)