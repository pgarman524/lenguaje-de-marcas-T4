import json
from jsonschema import validate

# Definir el esquema
schema = {
   {
    "Alumnado": {
      "Estudiante": [
        {
          "NIF": "12345678A",
          "Resultado": "apto",
          "Observaciones": "Buen estudiante",
          "IP": "192.168.1.1",
          "MAC": "null"
        },
        {
          "NIF": "23456789B",
          "Resultado": "No apto",
          "Observaciones": "Mal estudiante",
          "IP": "195.245.1.1",
          "MAC": "00:11:22:33:44:55"
        }
      ]
    }
  }
}

# Archivo JSON a validar
archivo_json = '''
{
    "Alumnado": {
      "Estudiante": [
        {
          "NIF": "12345678A",
          "Resultado": "apto",
          "Observaciones": "Buen estudiante",
          "IP": "192.168.1.1",
          "MAC": "null"
        },
        {
          "NIF": "23456789B",
          "Resultado": "No apto",
          "Observaciones": "Mal estudiante",
          "IP": "195.245.1.1",
          "MAC": "00:11:22:33:44:55"
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