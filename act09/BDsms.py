import json
from jsonschema import validate

# Definir el esquema
schema = {

  "$schema": "http://json-schema.org/draft-07/schema#",

  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "telefono": {
        "type": "string",
      # Para que en el validador te de error si no es de tamaño 9 el teléfono.
        "minLength":9
      },
      "fecha": {
        "type": "string",
      # Para añadir una restricción por patrón
        "pattern": "^\\d{2}-\\d{2}-\\d{4}$"
      },
      "hora": {
        "type": "string"
      },
      "mensaje": {
        "type": "string",
        #Añadir un min y max de palabras en el mensaje
        "minLength": 10,
        "maxLength":  500
      }
    },
    "required": [
      "telefono",
      "fecha",
      "hora",
      "mensaje"
      
    ]
  }

}

# Archivo JSON a validar
archivo_json = '''
[
    {
        "telefono": "955 55 66 55",
        "fecha": "1-7-2011",
        "hora": "23:55",
        "mensaje": "Juego1: Tetris"
    },
    {
        "telefono": "745 15 56 11",
        "fecha": "22-09-2011",
        "hora": "15:05",
        "mensaje": "Juego2: Arcanoid"
    },
    {
        "telefono": "842 35 22 00",
        "fecha": "10-11-2011",
        "hora": "09:22",
        "mensaje": "Juego3: Comecocos"
    }
]
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.