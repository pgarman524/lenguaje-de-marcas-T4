import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "mensajes": {
        "type": "object",
        "properties": {
          "m_pablo": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "tlf": {
                  "type": "number"
                },
                "fecha": {
                  "type": "string"
                },
                "hora": {
                  "type": "string"
                },
                "contenido": {
                  "type": "string"
                }
              },
              "required": [
                "tlf",
                "fecha",
                "hora",
                "contenido"
              ]
            }
          },
          "m_roberto": {
            "type": "object",
            "properties": {
              "tlf": {
                "type": "number"
              },
              "fecha": {
                "type": "string"
              },
              "hora": {
                "type": "string"
              },
              "contenido": {
                "type": "string"
              }
            },
            "required": [
              "tlf",
              "fecha",
              "hora",
              "contenido"
            ]
          }
        },
        "required": [
          "m_pablo",
          "m_roberto"
        ]
      }
    },
    "required": [
      "mensajes"
    ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "mensajes": {
      "m_pablo": [
        {
          "tlf": 123456789,
          "fecha": "11/01/2024",
          "hora": "12:00",
          "contenido": "¿Qué hay que hacer para lenguaje de marcas?"
        },
        {
          "tlf": 123456789,
          "fecha": "11/01/2024",
          "hora": "12:00",
          "contenido": "manda webs..."
        }
      ],
      "m_roberto": {
        "tlf": 987654321,
        "fecha": "12/01/2024",
        "hora": "9:00",
        "contenido": "Bro, me quedé dormido. No tengo ni idea"
      }
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