import json
from jsonschema import validate

# Definir el esquema
schema = {
 "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "peliculas": {
        "type": "object",
        "properties": {
          "pelicula": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "director": {
                  "type": "object",
                  "properties": {
                    "apellido1": {
                      "type": "string"
                    },
                    "apellido2": {
                      "type": "string"
                    },
                    "nombre": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "apellido1",
                    "apellido2",
                    "nombre"
                  ]
                },
                "titulo": {
                  "type": "string"
                },
                "fechaPublicacion": {
                  "type": "string"
                },
                "duracion": {
                  "type": "string"
                }
              },
              "required": [
                "director",
                "titulo",
                "fechaPublicacion",
                "duracion"
              ]
            }
          }
        },
        "required": [
          "pelicula"
        ]
      }
    },
    "required": [
      "peliculas"
    ]

}

# Archivo JSON a validar
archivo_json = '''
{
    "peliculas": {
      "pelicula": [
        {
          "director": {
            "apellido1": "King",
            "apellido2": "",
            "nombre": "Paul"
          },
          "titulo": "Wonka",
          "fechaPublicacion": "06/12/2023",
          "duracion": "1h57min"
        },
        {
          "director": {
            "apellido1": "Wan",
            "apellido2": "",
            "nombre": "James"
          },
          "titulo": "Aquaman y el reino perdido",
          "fechaPublicacion": "20/12/2023",
          "duracion": "2h04min"
        },
        {
          "director": {
            "apellido1": "Fernández",
            "apellido2": "Armero",
            "nombre": "Álvaro"
          },
          "titulo": "Ocho apellidos marroquís",
          "fechaPublicacion": "01/12/2023",
          "duracion": "1h35min"
        },
        {
          "director": {
            "apellido1": "Renner",
            "apellido2": "",
            "nombre": "Benjamin"
          },
          "titulo": "Migración. Un viaje patas arriba",
          "fechaPublicacion": "22/12/2023",
          "duracion": "1h22min"
        },
        {
          "director": {
            "apellido1": "Scott",
            "apellido2": "",
            "nombre": "Ridley"
          },
          "titulo": "Napoleón",
          "fechaPublicacion": "24/11/2023",
          "duracion": "2h38min"
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