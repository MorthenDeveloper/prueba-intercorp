import json
from flask import Flask, jsonify,request
from Models import db,Client
from logging import exception


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\client.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
#INICIA APP, VINCULA EL MODELO CON LA DB
db.init_app(app)

#ROUTES
@app.route("/")
def home():
    return "<h1>HOLAAA</h1>"

@app.route("/api/getClients",methods=["GET"])
def getClients():
    try:      
        clients = Client.query.all()
        toReturn = [client.serialize() for client in clients]
        return jsonify(toReturn), 200

    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}),500

@app.route("/api/getClients/<ID>",methods=["GET"]) 
def getClient(ID):
    try:      
        client = Client.query.filter_by(ID=ID).first()
        toReturn = [client.serialize()]

        if client is None:
            return jsonify({"msg": "El cliente no existe"}),404

        return jsonify(toReturn),200

    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}),500

if __name__ == "__main__":
    app.run(debug=True,port=4000)