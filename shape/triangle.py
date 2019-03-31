from flask import Blueprint, request, jsonify
from shape.models import Triangle, db
from shape import config

bp = Blueprint('triangle', __name__, url_prefix='/triangle')


@bp.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()

        if 'side_a' not in data:
            return jsonify({"error": "'side_a' is required"})

        if 'side_c' not in data:
            return jsonify({"error": "'side_c' is required"})

        if 'base' not in data:
            return jsonify({"error": "'base' is required"})

        if 'height' not in data:
            return jsonify({"error": "'height' is required"})

        tri = Triangle(**data)
        db.session.add(tri)
        db.session.commit()

        response_data = {
            "triangleData": {
                "id": tri.id,
                "side_a": tri.side_a,
                "side_c": tri.side_c,
                "base": tri.base,
                "height": tri.height,
            },
            "message": "Succesfully saved",
            "dataURL": {
                "areaURL":
                f"http://{config.HOST}:{config.PORT}/triangle/{tri.id}/area",
                "perimeterURL":
                f"http://{config.HOST}:{config.PORT}/triangle/{tri.id}/perimeter"
            }
        }

        return jsonify(response_data)


@bp.route('/<id>', methods=['GET', 'DELETE', 'PUT'])
def triangle(id):
    if request.method == 'GET':
        tri = Triangle.query.filter_by(id=id).first()

        if tri is None:
            return jsonify({"error": "ID not found"}), 404

        response_data = {
            "triangleData": {
                "id": tri.id,
                "side_a": tri.side_a,
                "side_c": tri.side_c,
                "base": tri.base,
                "height": tri.height,
            }
        }
        return jsonify(response_data)

    elif request.method == 'PUT':
        data = request.get_json()

        if 'side_a' not in data:
            return jsonify({"error": "'side_a' is required"})

        if 'side_c' not in data:
            return jsonify({"error": "'side_c' is required"})

        if 'base' not in data:
            return jsonify({"error": "'base' is required"})

        if 'height' not in data:
            return jsonify({"error": "'height' is required"})

        tri = Triangle.query.filter_by(id=id).first()

        if tri is None:
            return jsonify({"error": "ID not found"}), 404

        tri.side_a = data['side_a']
        tri.side_c = data['side_c']
        tri.base = data['base']
        tri.height = data['height']
        db.session.commit()

        response_data = {
            "triangleData": {
                "id": tri.id,
                "side_a": tri.side_a,
                "side_c": tri.side_c,
                "base": tri.base,
                "height": tri.height,
            },
            "message": "Succesfully updated",
            "dataURL": {
                "areaURL":
                f"http://{config.HOST}:{config.PORT}/triangle/{tri.id}/area",
                "perimeterURL":
                f"http://{config.HOST}:{config.PORT}/triangle/{tri.id}/perimeter"
            }
        }
        return jsonify(response_data)

    elif request.method == 'DELETE':
        tri = Triangle.query.filter_by(id=id).first()

        if tri is None:
            return jsonify({"error": "ID not found"}), 404

        db.session.delete(tri)
        db.session.commit()

        response_data = {"message": "Successfully deleted"}
        return jsonify(response_data)


@bp.route('/<id>/perimeter')
def perimeter(id):
    tri = Triangle.query.filter_by(id=id).first()

    if tri is None:
        return jsonify({"error": "ID not found"}), 404

    perimeter = tri.side_a + tri.base + tri.side_c
    response_data = {
        "triangleData": {
            "id": tri.id,
            "side_a": tri.side_a,
            "side_c": tri.side_c,
            "base": tri.base,
            "height": tri.height,
        },
        "message": f"The perimeter value is {perimeter}"
    }
    return jsonify(response_data)


@bp.route('/<id>/area')
def area(id):
    tri = Triangle.query.filter_by(id=id).first()

    if tri is None:
        return jsonify({"error": "ID not found"}), 404

    area = 0.5 * (tri.base * tri.height)

    response_data = {
        "triangleData": {
            "id": tri.id,
            "side_a": tri.side_a,
            "side_c": tri.side_c,
            "base": tri.base,
            "height": tri.height,
            "area": area,
        },
        "message": f"The area value is {area}"
    }
    return jsonify(response_data)
