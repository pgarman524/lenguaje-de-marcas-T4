import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "franquicia": {
        "type": "object",
        "properties": {
          "descripcion": {
            "type": "string"
          },
          "fecha": {
            "type": "string"
          },
          "barrio": {
            "type": "object",
            "properties": {
              "laMacarena": {
                "type": "object",
                "properties": {
                  "trimestres": {
                    "type": "object",
                    "properties": {
                      "trimestre1": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      },
                      "trimestre2": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      },
                      "trimestre3": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      },
                      "trimestre4": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      }
                    },
                    "required": [
                      "trimestre1",
                      "trimestre2",
                      "trimestre3",
                      "trimestre4"
                    ]
                  }
                },
                "required": [
                  "trimestres"
                ]
              },
              "pajaritos": {
                "type": "object",
                "properties": {
                  "trimestres": {
                    "type": "object",
                    "properties": {
                      "trimestre1": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      },
                      "trimestre2": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      },
                      "trimestre3": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      },
                      "trimestre4": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      }
                    },
                    "required": [
                      "trimestre1",
                      "trimestre2",
                      "trimestre3",
                      "trimestre4"
                    ]
                  }
                },
                "required": [
                  "trimestres"
                ]
              },
              "albaicin": {
                "type": "object",
                "properties": {
                  "trimestres": {
                    "type": "object",
                    "properties": {
                      "trimestre1": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      },
                      "trimestre2": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      },
                      "trimestre3": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      },
                      "trimestre4": {
                        "type": "object",
                        "properties": {
                          "beneficios": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "beneficios"
                        ]
                      }
                    },
                    "required": [
                      "trimestre1",
                      "trimestre2",
                      "trimestre3",
                      "trimestre4"
                    ]
                  }
                },
                "required": [
                  "trimestres"
                ]
              }
            },
            "required": [
              "laMacarena",
              "pajaritos",
              "albaicin"
            ]
          }
        },
        "required": [
          "descripcion",
          "fecha",
          "barrio"
        ]
      }
    },
    "required": [
      "franquicia"
    ]

}

# Archivo JSON a validar
archivo_json = '''
{
    "franquicia": {
      "descripcion": "Informe de beneficios de las franquicias alojadas en distintos barrios de la ciudad",
      "fecha": "12/05/2019",
      "barrio": {
        "laMacarena": {
          "trimestres": {
            "trimestre1": {
              "beneficios": 14995
            },
            "trimestre2": {
              "beneficios": 17889
            },
            "trimestre3": {
              "beneficios": 10040
            },
            "trimestre4": {
              "beneficios": 5023
            }
          }
        },
        "pajaritos": {
          "trimestres": {
            "trimestre1": {
              "beneficios": 45689
            },
            "trimestre2": {
              "beneficios": 21389
            },
            "trimestre3": {
              "beneficios": 35241
            },
            "trimestre4": {
              "beneficios": 27563
            }
          }
        },
        "albaicin": {
          "trimestres": {
            "trimestre1": {
              "beneficios": 1020
            },
            "trimestre2": {
              "beneficios": 2040
            },
            "trimestre3": {
              "beneficios": 1234
            },
            "trimestre4": {
              "beneficios": 789
            }
          }
        }
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