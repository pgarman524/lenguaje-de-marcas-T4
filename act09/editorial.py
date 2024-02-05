import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "editorial": {
        "type": "object",
        "properties": {
          "descripcion": {
            "type": "string"
          },
          "fecha": {
            "type": "string"
          },
          "region": {
            "type": "object",
            "properties": {
              "norte": {
                "type": "object",
                "properties": {
                  "trimestres": {
                    "type": "object",
                    "properties": {
                      "trimestre1": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "librosVendidos"
                        ]
                      },
                      "trimestre2": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "librosVendidos"
                        ]
                      },
                      "trimestre3": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "librosVendidos"
                        ]
                      },
                      "trimestre4": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "librosVendidos"
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
              "centro": {
                "type": "object",
                "properties": {
                  "trimestres": {
                    "type": "object",
                    "properties": {
                      "trimestre1": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "librosVendidos"
                        ]
                      },
                      "trimestre2": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "librosVendidos"
                        ]
                      },
                      "trimestre3": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "librosVendidos"
                        ]
                      },
                      "trimestre4": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "librosVendidos"
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
              "sur": {
                "type": "object",
                "properties": {
                  "trimestres": {
                    "type": "object",
                    "properties": {
                      "trimestre1": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "librosVendidos"
                        ]
                      },
                      "trimestre2": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "librosVendidos"
                        ]
                      },
                      "trimestre3": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "librosVendidos"
                        ]
                      },
                      "trimestre4": {
                        "type": "object",
                        "properties": {
                          "librosVendidos": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "librosVendidos"
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
              "norte",
              "centro",
              "sur"
            ]
          }
        },
        "required": [
          "descripcion",
          "fecha",
          "region"
        ]
      }
    },
    "required": [
      "editorial"
    ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "editorial": {
      "descripcion": "Informe de ventas para las regiones Norte, Centro y Sur",
      "fecha": "30/12/2009",
      "region": {
        "norte": {
          "trimestres": {
            "trimestre1": {
              "librosVendidos": 24000
            },
            "trimestre2": {
              "librosVendidos": 38600
            },
            "trimestre3": {
              "librosVendidos": "\"NO_INFO\""
            },
            "trimestre4": {
              "librosVendidos": "\"NO_INFO\""
            }
          }
        },
        "centro": {
          "trimestres": {
            "trimestre1": {
              "librosVendidos": "\"NO_INFO\""
            },
            "trimestre2": {
              "librosVendidos": 16080
            },
            "trimestre3": {
              "librosVendidos": 25000
            },
            "trimestre4": {
              "librosVendidos": 29000
            }
          }
        },
        "sur": {
          "trimestres": {
            "trimestre1": {
              "librosVendidos": 27000
            },
            "trimestre2": {
              "librosVendidos": 31400
            },
            "trimestre3": {
              "librosVendidos": 40100
            },
            "trimestre4": {
              "librosVendidos": 30000
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