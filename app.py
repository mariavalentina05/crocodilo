from flask import Flask, request
import psycopg
import requests
import json

app = Flask(__name__)

try:
    psycopg.connect("")
except psycopg.Error as e:
    print(f"Erro ao conectar ao banco: {e}")

@app.route("/consultar/<id>", methods=['GET'])
def consultar_id(id):
    return

@app.route("/consultar", methods=['GET'])
def consultar_nome():
    return