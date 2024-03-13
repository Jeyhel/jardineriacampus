import json 
import requests

def getAllGama():
    peticion= requests.get("")
    data = peticion.json()
    return data

def getAllNombre():
    