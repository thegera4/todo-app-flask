import os
from flask import Flask


# when using flask, you have to define the app in a function called create_app()
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        DATABASE_HOST=os.getenv("DB_HOST"),
        DATABASE_PASSWORD=os.getenv("MYSQL_ROOT_PASSWORD"),
        DATABASE_USER=os.getenv("MYSQL_ROOT_USER"),
        DATABASE=os.getenv("DB_NAME"),
    )

    from . import db

    db.init_app(app)

    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route("/hi")
    def hi():
        return "Hello World!"

    return app
