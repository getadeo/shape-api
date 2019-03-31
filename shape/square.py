from flask import Blueprint, request, jsonify
from shape.models import Square, db
from shape import config

bp = Blueprint('square', __name__, url_prefix='/square')


@bp.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()

        if 'side' not in data:
            return jsonify({"error": "'side' is required"})


        squ = Square(**data)
        db.session.add(squ)
        db.session.commit()

        response_data = {
            "squareData": {
                "id": squ.id,
                "side": squ.side,
            },
            "message": "Succesfully saved",
            "dataURL": {
                "areaURL":
                f"http://{config.HOST}:{config.PORT}/square/{squ.id}/area",
                "perimeterURL":
                f"http://{config.HOST}:{config.PORT}/square/{squ.id}/perimeter"
            }
        }

        return jsonify(response_data)


@bp.route('/<id>', methods=['GET', 'DELETE', 'PUT'])
def square(id):
    if request.method == 'GET':
        squ = Square.query.filter_by(id=id).first()

        if squ is None:
            return jsonify({"error": "ID not found"}), 404

        response_data = {
            "squareData": {
                "id": squ.id,
                "side": squ.side,
            }
        }
        return jsonify(response_data)

    elif request.method == 'PUT':
        data = request.get_json()

        if 'side' not in data:
            return jsonify({"error": "'side' is required"})

        squ = Square.query.filter_by(id=id).first()

        if squ is None:
            return jsonify({"error": "ID not found"}), 404

        squ.side = data['side']
        db.session.commit()

        response_data = {
            "squareData": {
                "id": squ.id,
                "side": squ.side,
            },
            "message": "Succesfully updated",
            "dataURL": {
                "areaURL":
                f"http://{config.HOST}:{config.PORT}/square/{squ.id}/area",
                "perimeterURL":
                f"http://{config.HOST}:{config.PORT}/square/{squ.id}/perimeter"
            }
        }
        return jsonify(response_data)

    elif request.method == 'DELETE':
        squ = Square.query.filter_by(id=id).first()

        if squ is None:
            return jsonify({"error": "ID not found"}), 404

        db.session.delete(squ)
        db.session.commit()

        response_data = {"message": "Successfully deleted"}
        return jsonify(response_data)


@bp.route('/<id>/perimeter')
def perimeter(id):
    squ = Square.query.filter_by(id=id).first()

    if squ is None:
        return jsonify({"error": "ID not found"}), 404

    perimeter = float(4 * squ.side)
    response_data = {
        "squareData": {
            "id": squ.id,
            "side": squ.side,
            "perimeter": perimeter,
        },
        "message": f"The perimeter value is {perimeter}"
    }
    return jsonify(response_data)


@bp.route('/<id>/area')
def area(id):
    squ = Square.query.filter_by(id=id).first()

    if squ is None:
        return jsonify({"error": "ID not found"}), 404

    area = float(squ.side * squ.side)
    response_data = {
        "squareData": {
            "id": squ.id,
            "side": squ.side,
            "area": area,
        },
        "message": f"The area value is {area}"
    }
    return jsonify(response_data)
