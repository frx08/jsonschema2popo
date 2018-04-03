# JSONSCHEMA2POPO

A converter to extract 'Plain Old Python Object' classes from JSON Schema files.
Currenty compatible with python 3.4+

## Installation

    pip install jsonschema2popo

## Usage

Basic:

    jsonschema2popo -o /path/to/output_file.py /path/to/json_schema.json
    
object JSON encoding:

    import json
    
    g = GeneratedClass()
    json.dumps(g.as_dict())
