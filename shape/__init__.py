from flask import Flask
from shape import config
from shape import models


def create_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'Hello'

    from shape import rectangle, square, triangle
    app.register_blueprint(rectangle.bp)
    app.register_blueprint(square.bp)
    app.register_blueprint(triangle.bp)

    app.config.from_object(config)

    print(config.SQLALCHEMY_DATABASE_URI)

    models.init_app(app)

    return app
