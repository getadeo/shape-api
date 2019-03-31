import shape
from shape import models

app = shape.create_app()

with app.app_context():
    models.db.create_all()