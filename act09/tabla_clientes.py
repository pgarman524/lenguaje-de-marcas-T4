import json
from jsonschema import validate

# Definir el esquema
schema = {

  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "Clientes": {
      "type": "object",
      "properties": {
        "sede": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "cod_sede": {
                "type": "string"
              },
              "direccion1": {
                "type": "string"
              },
              "direccion2": {
                "type": "string"
              },
              "empleado": {
                "type": "string"
              },
              "fecha": {
                "type": "string"
              },
              "clientela": {}
            },
            "required": [
              "cod_sede",
              "direccion1",
              "direccion2",
              "empleado",
              "fecha",
              "clientela"
            ]
          }
        }
      },
      "required": [
        "sede"
      ]
    }
  },
  "required": [
    "Clientes"
  ]

}

# Archivo JSON a validar
archivo_json = '''
{
    "Clientes": {
      "sede": [
        {
          "cod_sede": "",
          "direccion1": "Calle falsa 123",
          "direccion2": "Calle no tan falsa 456",
          "empleado": "",
          "fecha": "12/02/24",
          "clientela": [
            {
              "descripcion": "solvente",
              "numero": 3,
              "vivienda": [
                {
                  "coste": 100000,
                  "resumen": "Casa antigua",
                  "plazo": 45
                },
                {
                  "coste": 85000,
                  "resumen": "Casa antigua para reformar",
                  "plazo": 35
                },
                {
                  "coste": 325000,
                  "resumen": "Casa reformada",
                  "plazo": 70
                }
              ]
            },
            {
              "descripcion": "insolvente",
              "numero": 1,
              "vivienda": {
                "coste": 75000,
                "resumen": "Casa antigua sin reformar",
                "plazo": 68
              }
            }
          ]
        },
        {
          "cod_sede": "",
          "direccion1": "Calle falsa 123",
          "direccion2": "Calle no tan falsa 456",
          "empleado": "",
          "fecha": "16/05/14",
          "clientela": {
            "descripcion": "solvente",
            "numero": 1,
            "vivienda": {
              "coste": 95000,
              "resumen": "Casa antigua sin reformar",
              "plazo": 98
            }
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