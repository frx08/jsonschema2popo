# JSONSCHEMA2POPO

A converter to extract 'Plain Old Python Object' classes from JSON Schema files.
Currenty compatible with python 3.4+

## Installation

    git clone https://github.com/frx08/jsonschema2popo.git
    cd jsonschema2popo
    pip install -r requirements.txt

## Usage

Basic:

    python jsonschema2popo.py -o /path/to/output_file.py /path/to/json_schema.json
    
object JSON encoding:

    import json
    
    g = GeneratedClass()
    json.dumps(g.as_dict())
