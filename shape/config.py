import os

SQLALCHEMY_DATABASE_URI = os.getenv(
  'SQLALCHEMY_DATABASE_URI',
  'sqlite:///' + os.path.dirname(os.path.abspath(__name__)) + '/shape/db/shapes.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False
HOST = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
PORT = os.getenv('FLASK_RUN_PORT', 5000)