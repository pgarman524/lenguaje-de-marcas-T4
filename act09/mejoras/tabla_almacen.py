import json
from jsonschema import validate

# Definir el esquema
schema = {

    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Sede": {
        "type": "object",
        "properties": {
          "Almacen": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "cod_sede": {
                  "type": "number"
                },
                "direccion1": {
                  "type": "string"
                },
                "direccion2": {
                  "type": "string"
                },
                "gerente": {
                  "type": "string"
                },
                "fecha": {
                  "type": "string"
                },
                "Seccion": {}
              },
              "required": [
                "cod_sede",
                "direccion1",
                "direccion2",
                "gerente",
                "fecha",
                "Seccion"
              ]
            }
          }
        },
        "required": [
          "Almacen"
        ]
      }
    },
    "required": [
      "Sede"
    ]


}

# Archivo JSON a validar
archivo_json = '''
{
    "Sede": {
      "Almacen": [
        {
          "cod_sede": 33,
          "direccion1": "Calle falsa 123",
          "direccion2": "",
          "gerente": "ASA-808",
          "fecha": "12/02/24",
          "Seccion": [
            {
              "descripcion": "Salón",
              "numero": 2,
              "producto": [
                {
                  "coste": 189,
                  "resumen": "KIVIK",
                  "plazo": 12
                },
                {
                  "coste": 99.99,
                  "resumen": "STRANDMON",
                  "plazo": 3
                }
              ]
            },
            {
              "descripcion": "Cocina",
              "numero": 4,
              "producto": [
                {
                  "coste": 405,
                  "resumen": "KNOXHULT",
                  "plazo": 12
                },
                {
                  "coste": 59,
                  "resumen": "EKEDALEN",
                  "plazo": 0
                },
                {
                  "coste": 59,
                  "resumen": "EKEDALEN",
                  "plazo": 0
                },
                {
                  "coste": 69,
                  "resumen": "KNOXHULT",
                  "plazo": 1
                }
              ]
            }
          ]
        },
        {
          "cod_sede": 45,
          "direccion1": "Calle no tan falsa 123",
          "direccion2": "",
          "gerente": "CAS-128",
          "fecha": "25/02/24",
          "Seccion": {
            "descripcion": "Dormitorio",
            "numero": 2,
            "producto": [
              {
                "coste": 586,
                "resumen": "BRIMNES",
                "plazo": 0
              },
              {
                "coste": 656.98,
                "resumen": "SONGESAND",
                "plazo": 3
              }
            ]
          }
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