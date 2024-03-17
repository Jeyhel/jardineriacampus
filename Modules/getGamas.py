#import json 
import requests

def getAllGama():
    peticion= requests.get("http://172.16.103.33:5527")
    data = peticion.json()
    return data

def getAllNombre():
      gamaNombre = []
      for val in getAllGama():
          gamaNombre.append(val.get("gama"))
      return gamaNombre
