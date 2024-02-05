import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Libreria": {
        "type": "object",
        "properties": {
          "libro": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "ISBN": {
                  "type": "number"
                },
                "titulo": {
                  "type": "string"
                },
                "autor": {
                  "type": "string"
                },
                "disponible": {
                  "type": "string"
                },
                "notas": {
                  "type": "string"
                },
                "descripcion": {
                  "type": "string"
                }
              },
              "required": [
                "ISBN",
                "titulo",
                "autor",
                "disponible"
              ]
            }
          }
        },
        "required": [
          "libro"
        ]
      }
    },
    "required": [
      "Libreria"
    ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "Libreria": {
      "libro": [
        {
          "ISBN": 1234567890,
          "titulo": "EL Lazarillo de Tormes",
          "autor": "none",
          "disponible": "no",
          "notas": "null"
        },
        {
          "ISBN": 987654321,
          "titulo": "Harry Potter",
          "autor": "JK. Rowlin",
          "disponible": "sí",
          "descripcion": "Ta' perfe"
        }
      ]
    }
  }
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.