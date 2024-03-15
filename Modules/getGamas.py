#import json 
import requests

def getAllGama():
    peticion= requests.get("http://172.16.100.144:5869")
    data = peticion.json()
    return data

def getAllNombre():
      gamaNombre = []
      for val in getAllGama():
          gamaNombre.append(val.get("gama"))
      return gamaNombre
