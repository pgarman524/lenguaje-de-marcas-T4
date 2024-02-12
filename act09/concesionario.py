import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "Concesionario": {
            "type": "object",
            "properties": {
                "concesionario": {
                    "type": "object",
                    "properties": {
                        "cod_coche": {
                            "type": "string",
                           "minLength":1
                        },
                        "marca": {
                            "type": "string",
                            "minimum":  1,
                            "maximum":  20                                                                    
                        },
                        "modelo": {
                            "type": "string",
                             "minimum":  1,
                            "maximum":  30  
                        },
                        "matricula": {
                            "type": "string",
                            "pattern": "^[0-9]{8}[a-zA-Z]$"
                        },
                        "potencia": {
                            "type": "string",
                             "minimum":  1,
                            "maximum":  20  
                        },
                        "plazas": {
                            "type": "number",
                             "minimum":  2,
                            "maximum":  8  
                        },
                        "num_puertas": {
                            "type": "number",
                             "minimum":  2,
                            "maximum":  8  
                        }
                    },
                    "required": [
                        "cod_coche",
                        "marca",
                        "modelo",
                        "matricula",
                        "potencia",
                        "plazas",
                        "num_puertas"
                    ]
                }
            },
            "required": [
                "concesionario"
            ]
        }
    },
    "required": [
        "Concesionario"
    ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "Concesionario": {
        "concesionario": {
            "cod_coche": "" ,
            "marca": "CITROEN",
            "modelo": "C3 Aircross PureTech",
            "matricula": "56748912A",
            "potencia": "110CV",
            "plazas":  5,
            "num_puertas":  4
        }
    }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

# Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON,  
# y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción.  
# En caso contrario, se lanzará una excepción indicando la razón de la invalidación.
