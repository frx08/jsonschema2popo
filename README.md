# JSONSCHEMA2POPO

A converter to extract 'Plain Old Python Object' classes from JSON Schema files.
Currenty compatible with python 3.4+

## Installation

    git clone https://github.com/frx08/jsonschema2popo.git
    cd jsonschema2popo
    pip install -r requirements.txt

## Usage

Basic:

    python jsonschema2popo.py /path/to/json_schema.json -o /path/to/output_folder/

object JSON encoding:

    g = GeneratedClass()
    json.dumps(g, cls=generated_module.Encoder)
