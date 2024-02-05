import json
from jsonschema import validate

# Definir el esquema
schema = {

    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
      "Mueble": {
        "type": "object",
        "properties": {
          "mueble": {
            "type": "object",
            "properties": {
              "cod_mueble": {
                "type": "string"
              },
              "tipo": {
                "type": "string"
              },
              "modelo": {
                "type": "string"
              },
              "num_almacen": {
                "type": "number"
              },
              "dificultad_ensamblaje": {
                "type": "string"
              },
              "materiales": {
                "type": "string"
              },
              "lugar_uso": {
                "type": "string"
              }
            },
            "required": [
              "cod_mueble",
              "tipo",
              "modelo",
              "num_almacen",
              "dificultad_ensamblaje",
              "materiales",
              "lugar_uso"
            ]
          }
        },
        "required": [
          "mueble"
        ]
      }
    },
    "required": [
      "Mueble"
    ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "Mueble": {
      "mueble": {
        "cod_mueble": "004.729.62",
        "tipo": "sofas",
        "modelo": "BOLLSTANÄS",
        "num_almacen": 5700,
        "dificultad_ensamblaje": "easy",
        "materiales": "poliester",
        "lugar_uso": "salon"
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