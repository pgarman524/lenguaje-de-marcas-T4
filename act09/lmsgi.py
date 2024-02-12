import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "modulos": {
        "type": "object",
        "properties": {
          "modulo": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "nombre": {
                  "type": "string",
                  "maxLength":120
                },
                "contenido": {
                  "type": "object",
                  "properties": {
                    "unidad": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "num": {
                            "type": "number",
                              "minLength":1,
                              "maxLength":20
                          },
                          "titulo": {
                            "type": "string",
                            "maxLength":120
                          },
                          "descripcion": {
                            "type": "string",
                            "maxLength":400
                          }
                        },
                        "required": [
                          "num",
                          "titulo",
                          "descripcion"
                        ]
                      }
                    }
                  },
                  "required": [
                    "unidad"
                  ]
                }
              },
              "required": [
                "nombre",
                "contenido"
              ]
            }
          }
        },
        "required": [
          "modulo"
        ]
      }
    },
    "required": [
      "modulos"
    ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "modulos": {
      "modulo": [
        {
          "nombre": "Lenguajes de Marcas y Sistemas de Gestión de Información",
          "contenido": {
            "unidad": [
              {
                "num": 1,
                "titulo": "Interpretación de lenguajes de marcas",
                "descripcion": "Esta unidad cubre la interpretación de los lenguajes de marcas, incluyendo la identificación de sus características principales y elementos. También se abordan las ventajas de estos lenguajes en el tratamiento de la información y su clasificación."
              },
              {
                "num": 2,
                "titulo": "Características del lenguaje XML",
                "descripcion": "En esta unidad, los estudiantes aprenden sobre las características propias del lenguaje XML, incluyendo la estructura de un documento XML y sus reglas sintácticas. También se discuten las ventajas que aportan los espacios de nombres."
              },
              {
                "num": 3,
                "titulo": "Conversión y adaptación de documentos XML",
                "descripcion": "Esta unidad cubre la conversión de documentos XML y las técnicas de transformación de estos documentos. También se abordan las especificaciones de conversión y la utilización de plantillas y herramientas de procesamiento."
              },
              {
                "num": 4,
                "titulo": "Gestión y almacenamiento de información en formatos XML",
                "descripcion": "En esta unidad, los estudiantes aprenden sobre los sistemas de almacenamiento de información en formato XML y las ventajas e inconvenientes de estos sistemas. También se discuten los sistemas gestores de bases de datos relacionales y documentos XML, así como los sistemas gestores de bases de datos nativas XML."
              }
            ]
          }
        },
        {
          "nombre": "Sistemas Informáticos",
          "contenido": {
            "unidad": [
              {
                "num": 1,
                "titulo": "Hardware de un sistema informático",
                "descripcion": "Esta unidad cubre los componentes físicos de un ordenador actual, incluyendo la arquitectura hardware, los periféricos, las unidades de entrada/salida, y el montaje y puesta en marcha de un ordenador."
              },
              {
                "num": 2,
                "titulo": "Software de un sistema informático",
                "descripcion": "En esta unidad, los estudiantes aprenden sobre el software que se utiliza en un sistema informático, aunque no se proporcionan detalles específicos en la fuente proporcionada."
              },
              {
                "num": 3,
                "titulo": "Redes de ordenadores",
                "descripcion": "Esta unidad cubre las características de las redes de ordenadores, la arquitectura de red, las topologías de red y los modos de conexión, los componentes de una red informática, las redes inalámbricas 802.11, el direccionamiento IP, la seguridad, la configuración de routers, y los servicios de red."
              },
              {
                "num": 4,
                "titulo": "Administración básica de sistemas (GNU/Linux)",
                "descripcion": "En esta unidad, los estudiantes aprenden los fundamentos de la administración de sistemas en GNU/Linux."
              }
            ]
          }
        },
        {
          "nombre": "Bases de Datos",
          "contenido": {
            "unidad": [
              {
                "num": 1,
                "titulo": "Interpretación del diseño lógico de bases de datos",
                "descripcion": "Esta unidad se enfoca en interpretar el diseño lógico de las bases de datos, analizando y cumpliendo las especificaciones relativas a su aplicación para gestionar bases de datos."
              },
              {
                "num": 2,
                "titulo": "Selección y uso de lenguajes, herramientas y librerías",
                "descripcion": "En esta unidad, los estudiantes aprenden a seleccionar y emplear lenguajes, herramientas y librerías, interpretando las especificaciones para desarrollar aplicaciones multiplataforma con acceso a bases de datos."
              },
              {
                "num": 3,
                "titulo": "Gestión de la información almacenada",
                "descripcion": "Esta unidad cubre la gestión de la información almacenada, planificando e implementando sistemas de formularios e informes para desarrollar aplicaciones de gestión."
              },
              {
                "num": 4,
                "titulo": "Realización de consultas",
                "descripcion": "En esta unidad, los estudiantes aprenden a realizar consultas, analizando y evaluando su alcance, para gestionar la información almacenada en sistemas ERP/CRM."
              }
            ]
          }
        },
        {
          "nombre": "Programación",
          "contenido": {
            "unidad": [
              {
                "num": 1,
                "titulo": "Introducción a la programación",
                "descripcion": "Esta unidad proporciona una introducción a los conceptos básicos de la programación, incluyendo la estructura de un programa informático y cómo reconocer y relacionar los elementos propios del lenguaje de programación utilizado."
              },
              {
                "num": 2,
                "titulo": "Uso de estructuras de control",
                "descripcion": "En esta unidad, los estudiantes aprenden sobre las estructuras de control en la programación, como bucles y condicionales."
              },
              {
                "num": 3,
                "titulo": "Utilización de objetos",
                "descripcion": "Esta unidad cubre los fundamentos de la programación orientada a objetos, incluyendo la definición de clases y objetos, la interacción entre objetos, y el uso de métodos y propiedades de los objetos."
              },
              {
                "num": 4,
                "titulo": "Desarrollo de clases",
                "descripcion": "En esta unidad, los estudiantes aprenden a desarrollar programas organizados en clases, analizando y aplicando los principios de la programación orientada a objetos. Esto incluye la declaración de clases, la estructura y miembros de una clase, la encapsulación, control de acceso y visibilidad, y la utilización de los métodos y atributos de una clase."
              }
            ]
          }
        },
        {
          "nombre": "Entornos de Desarrollo",
          "contenido": {
            "unidad": [
              {
                "num": 1,
                "titulo": "Introducción a los entornos de desarrollo",
                "descripcion": "Esta unidad proporciona una introducción a los entornos de desarrollo, explicando qué son, cómo funcionan y por qué son importantes en el desarrollo de software."
              },
              {
                "num": 2,
                "titulo": "Configuración de entornos de desarrollo",
                "descripcion": "En esta unidad, los estudiantes aprenden a configurar entornos de desarrollo, incluyendo la instalación y configuración de herramientas y librerías necesarias para el desarrollo de aplicaciones."
              },
              {
                "num": 3,
                "titulo": "Uso de entornos de desarrollo",
                "descripcion": "Esta unidad cubre cómo utilizar los entornos de desarrollo, incluyendo la escritura, prueba y depuración de código, así como la colaboración y el control de versiones."
              },
              {
                "num": 4,
                "titulo": "Implementación de aplicaciones en entornos de desarrollo",
                "descripcion": "En esta unidad, los estudiantes aprenden a implementar aplicaciones en entornos de desarrollo, incluyendo la preparación de aplicaciones para la producción y la gestión de la calidad del software."
              }
            ]
          }
        },
        {
          "nombre": "Formación y Orientación Laboral",
          "contenido": {
            "unidad": [
              {
                "num": 1,
                "titulo": "Derecho del Trabajo",
                "descripcion": "Esta unidad cubre los aspectos legales relacionados con el trabajo, incluyendo los derechos y obligaciones de los empleadores y empleados, y los aspectos legales de los contratos de trabajo."
              },
              {
                "num": 2,
                "titulo": "Seguridad Social y Desempleo",
                "descripcion": "En esta unidad, los estudiantes aprenden sobre la Seguridad Social, los derechos de los trabajadores en caso de desempleo, y cómo se maneja la situación de desempleo en España."
              },
              {
                "num": 3,
                "titulo": "Prevención de Riesgos Laborales",
                "descripcion": "Esta unidad cubre los conceptos básicos de la prevención de riesgos laborales, los factores de riesgo y cómo prevenirlos, y la legislación y organización relacionadas con la prevención de riesgos laborales."
              },
              {
                "num": 4,
                "titulo": "Orientación Laboral",
                "descripcion": "En esta unidad, los estudiantes aprenden sobre la orientación laboral, incluyendo cómo buscar empleo, cómo prepararse para una entrevista de trabajo, y cómo prepararse para el primer día de trabajo."
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