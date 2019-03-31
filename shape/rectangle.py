from flask import Blueprint, request, jsonify
from shape.models import Rectangle, db
from shape import config

bp = Blueprint('rectangle', __name__, url_prefix='/rectangle')

@bp.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()

        if 'length' not in data:
            return jsonify({"error": "'length' is required"})

        if 'width' not in data:
            return jsonify({"error": "'width' is required"})

        rec = Rectangle(**data)
        db.session.add(rec)
        db.session.commit()

        response_data = {
            "rectangleData": {
                "id": rec.id,
                "length": rec.length,
                "width": rec.width,
            },
            "message": "Succesfully saved",
            "dataURL": {
                "areaURL": f"http://{config.HOST}:{config.PORT}/rectangle/{rec.id}/area",
                "perimeterURL": f"http://{config.HOST}:{config.PORT}/rectangle/{rec.id}/perimeter"
            }
        }

        return jsonify(response_data)

@bp.route('/<id>', methods=['GET', 'DELETE', 'PUT'])
def rectangle(id):
    if request.method == 'GET':
        rec = Rectangle.query.filter_by(id=id).first()

        if rec is None:
            return jsonify({"error": "ID not found"}), 404

        response_data = {
            "rectangleData": {
                "id": rec.id,
                "length": rec.length,
                "width": rec.width,
            }
        }
        return jsonify(response_data)


    elif request.method == 'PUT':
        data = request.get_json()

        if 'length' not in data:
            return jsonify({"error": "'length' is required"})

        if 'width' not in data:
            return jsonify({"error": "'width' is required"})

        rec = Rectangle.query.filter_by(id=id).first()

        if rec is None:
            return jsonify({"error": "ID not found"}), 404

        rec.length = data['length']
        rec.width = data['width']
        db.session.commit()

        response_data = {
            "rectangleData": {
                "id": rec.id,
                "length": rec.length,
                "width": rec.width
            },
            "message": "Succesfully updated",
            "dataURL": {
                "areaURL":
                f"http://{config.HOST}:{config.PORT}/rectangle/{rec.id}/area",
                "perimeterURL":
                f"http://{config.HOST}:{config.PORT}/rectangle/{rec.id}/perimeter"
            }
        }
        return jsonify(response_data)

    elif request.method == 'DELETE':
        rec = Rectangle.query.filter_by(id=id).first()

        if rec is None:
            return jsonify({
              "error": "ID not found"
            }), 404

        db.session.delete(rec)
        db.session.commit()

        response_data = {
          "message": "Succesfully Deleted"
        }
        return jsonify(response_data)


@bp.route('/<id>/perimeter')
def perimeter(id):
    rec = Rectangle.query.filter_by(id=id).first()

    if rec is None:
        return jsonify({"error": "ID not found"}), 404

    perimeter = float(2 * (rec.length + rec.width))
    response_data = {
      "rectangleData": {
        "id": rec.id,
        "length": rec.length,
        "width": rec.width,
        "perimeter": perimeter,
      },
      "message": f"The perimeter value is {perimeter}"
    }
    return jsonify(response_data)


@bp.route('/<id>/area')
def area(id):
    rec = Rectangle.query.filter_by(id=id).first()

    if rec is None:
        return jsonify({"error": "ID not found"}), 404

    area = float(rec.length + rec.width)
    response_data = {
        "rectangleData": {
            "id": rec.id,
            "length": rec.length,
            "width": rec.width,
            "area": area,
        },
        "message": f"The area value is {area}"
    }
    return jsonify(response_data)
