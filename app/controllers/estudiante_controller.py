from flask import jsonify,request,Blueprint
from app.utils.decorator import jwt_required,roles_required
from app.views.estudiante_view import render_estudiante_detail,render_estudiante_list
from app.models.estudiantes_model import Estudiante

estudiante_bp=Blueprint("estudiante",__name__)

@estudiante_bp.route("/estudiantes",methods=["GET"])
@jwt_required 
@roles_required(roles=["admin","user"])
def get_estudiantes():
    estudiantes=Estudiante.get_all()
    return jsonify(render_estudiante_list(estudiantes))

@estudiante_bp.route("/estudiantes/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_estudiantes_id(id):
    estudiante=Estudiante.get_by_id(id)
    if not estudiante:
        return jsonify({"error":"Producto no encontrado"}),404
    return jsonify(render_estudiante_detail(estudiante))

@estudiante_bp.route("/estudiantes",methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_estudiante():
    data=request.json
    nombre=data.get("nombre") 
    edad=data.get("edad")
    peso=data.get("peso")
    bueno=data.get("bueno")
    
    if nombre is None or edad is None or peso is None or bueno is None:
        return jsonify({"error":"Faltan datos requeridos"}),400
    
    estudiante=Estudiante(nombre=nombre,edad=int(edad),peso=float(peso),bueno=bool(bueno))
    estudiante.save()
    return jsonify(render_estudiante_detail(estudiante)),201
    
@estudiante_bp.route("/estudiantes/<int:id>",methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def actualizar_student(id):
    estudent=Estudiante.get_by_id(id)
    if not estudent:
        return jsonify({"error":"Producto no encontrado"}),404
    data=request.json
    nombre=data.get("nombre")
    edad=data.get("edad")
    peso=data.get("peso")
    bueno=data.get("bueno")
    estudent.update(nombre=nombre,edad=int(edad),peso=float(peso),bueno=bool(bueno))
    return jsonify(render_estudiante_detail(estudent))


@estudiante_bp.route("/estudiantes/<int:id>",methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_estudiante(id):
    estudiante=Estudiante.get_by_id(id)
    if not estudiante:
        return jsonify({"error":"Producto no encontrado"}),404
    estudiante.delete()
    return "",204