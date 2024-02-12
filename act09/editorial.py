import json
from jsonschema import validate

# Define the schema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "editorial": {
            "type": "object",
            "properties": {
                "descripcion": {"type": "string",
                                "minLength": 10,
                                 "maxLength":  500
                                },
                "fecha": {"type": "string",
                          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
                "region": {
                    "type": "object",
                    "properties": {
                        "norte": {"type": "object"},
                        "centro": {"type": "object"},
                        "sur": {"type": "object"}
                    },
                    "required": ["norte", "centro", "sur"]
                }
            },
            "required": ["descripcion", 
                         "fecha", 
                         "region"]
        }
    },
    "required": ["editorial"]
}

# JSON object to validate
archivo_json = '''
{
    "editorial": {
        "descripcion": "Informe de ventas para las regiones Norte, Centro y Sur",
        "fecha": "2009-12-30",
        "region": {
            "norte": {},
            "centro": {},
            "sur": {}
        }
    }
}
'''

# Load the JSON object
datos_json = json.loads(archivo_json)

# Validate the JSON object against the schema
try:
    validate(instance=datos_json, schema=schema)
    print("JSON is valid.")
except Exception as e:
    print(f"Validation error: {e}")
