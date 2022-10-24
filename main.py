from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorMateria import ControladorMateria
from Controladores.ControladorInscripcion import ControladorInscripcion
from Controladores.ControladorCandidatos import ControladorCandidatos
miControladorEstudiante=ControladorEstudiante()
miControladorDepartamento=ControladorDepartamento()
miControladorMateria=ControladorMateria()
miControladorInscripcion=  ControladorInscripcion()
miControladorCandidato = ControladorCandidatos()

###################################################################################
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
########################mesas###########################################################
@app.route("/mesas",methods=['GET'])
def getEstudiantes():
    json=miControladorEstudiante.index()
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=miControladorEstudiante.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorEstudiante.show(id)
    return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=miControladorEstudiante.update(id,data)
    return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=miControladorEstudiante.delete(id)
    return jsonify(json)
############################partidos#######################################################
@app.route("/departamentos",methods=['GET'])
def getDepartamentos():
    json=miControladorDepartamento.index()
    return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['GET'])
def getDepartamento(id):
    json=miControladorDepartamento.show(id)
    return jsonify(json)
@app.route("/departamentos",methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    json=miControladorDepartamento.create(data)
    return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['PUT'])
def modificarDepartamento(id):
    data = request.get_json()
    json=miControladorDepartamento.update(id,data)
    return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['DELETE'])
def eliminarDepartamento(id):
    json=miControladorDepartamento.delete(id)
    return jsonify(json)
################################candidatos###################################################
@app.route("/candidatos",methods=['GET'])
def getMaterias():
    json=miControladorCandidato.index()
    print("Get conseguido")
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getMateria(id):
    json=miControladorCandidato.show(id)
    print("Get by id conseguido")
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearMateria():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    print("Post conseguido")
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarMateria(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    print("Put conseguido")
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarMateria(id):
    json=miControladorCandidato.delete(id)
    print("Delete conseguido")
    return jsonify(json)
#@app.route("/materias/<string:id>/departamento/<string:id_departamento>",methods=['PUT'])
#def asignarDepartamentoAMateria(id,id_departamento):
#    json=miControladorMateria.asignarDepartamento(id,id_departamento)
#    return jsonify(json)
##################################resultados#################################################
@app.route("/inscripciones",methods=['GET'])
def getInscripciones():
    json=miControladorInscripcion.index()
    return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['GET'])
def getInscripcion(id):
    json=miControladorInscripcion.show(id)
    return jsonify(json)
@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.create(data,id_estudiante,id_materia)
    return jsonify(json)
@app.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['PUT'])
def modificarInscripcion(id_inscripcion,id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.update(id_inscripcion,data,id_estudiante,id_materia)
    return jsonify(json)
@app.route("/inscripciones/<string:id_inscripcion>",methods=['DELETE'])
def eliminarInscripcion(id_inscripcion):
    json=miControladorInscripcion.delete(id_inscripcion)
    return jsonify(json)
###################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])