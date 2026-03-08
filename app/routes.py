from flask import Blueprint, request, jsonify
from app import db
from app.models import Student

main = Blueprint("main", __name__)

@main.route("/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "healthy"}), 200


@main.route("/api/v1/students", methods=["POST"])
def add_student():
    data = request.get_json()

    student = Student(
        name=data["name"],
        age=data["age"],
        department=data["department"]
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Student added successfully"}), 201


@main.route("/api/v1/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    result = []

    for student in students:
        result.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "department": student.department
        })

    return jsonify(result), 200


@main.route("/api/v1/students/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    return jsonify({
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "department": student.department
    }), 200


@main.route("/api/v1/students/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    data = request.get_json()

    student.name = data["name"]
    student.age = data["age"]
    student.department = data["department"]

    db.session.commit()

    return jsonify({"message": "Student updated successfully"}), 200


@main.route("/api/v1/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted successfully"}), 200
