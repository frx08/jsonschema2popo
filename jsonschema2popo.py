#!/usr/bin/env python

import os
import argparse
import json
from jinja2 import Environment, FileSystemLoader

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class JsonSchema2Popo:
    """Converts a JSON Schema to a Plain Old Python Object class"""

    TEMPLATES_FOLDER = 'templates/'
    CLASS_TEMPLATE_FNAME = '_class.tmpl'
    
    J2P_TYPES = {
        'string': str,
        'integer': int,
        'number': float,
        'object': type,
        'array': list,
        'boolean': bool,
        'null': None
    }
    
    def __init__(self):
        self.jinja = Environment(loader=FileSystemLoader(os.path.join(os.path.sep, SCRIPT_DIR, self.TEMPLATES_FOLDER)), trim_blocks=True)
        
        self.definitions = []

    def load(self, json_schema_file):
        self.process(json.load(json_schema_file))

    def process(self, json_schema):
        for _obj_name, _obj in json_schema['definitions'].items():
            model = self.definition_parser(_obj_name, _obj)
            self.definitions.append(model)
        
        # oreder definition
        changes = []
        model_names = [m['name'] for m in self.definitions]
        for model in self.definitions:
            for prop in model['properties']:
                if prop['_type']['type'] in model_names:
                    changes.append([model['name'], prop['_type']['type']])
                elif prop['_type']['subtype'] in model_names:
                    changes.append([model['name'], prop['_type']['subtype']])
        for change in changes:
            model_names = [m['name'] for m in self.definitions]
            newindex = model_names.index(change[0])
            oldindex = model_names.index(change[1])
            self.definitions.insert(newindex, self.definitions.pop(oldindex))
        
        # root object
        if 'title' in json_schema:
            root_object_name = ''.join(x for x in json_schema['title'].title() if x.isalpha())
        else:
            root_object_name = 'RootObject'
        root_model = self.definition_parser(root_object_name, json_schema)
        self.definitions.append(root_model)

    def definition_parser(self, _obj_name, _obj):
        model = {}
        model['name'] = _obj_name
        if 'type' in _obj:
            model['type'] = self.type_parser(_obj)

        model['properties'] = []
        if 'properties' in _obj:
            for _prop_name, _prop in _obj['properties'].items():
                _type = self.type_parser(_prop)
                _default = None
                if 'default' in _prop:
                    _default = _type['type'](_prop['default'])
                    if _type['type'] == str:
                        _default = "'{}'".format(_default)

                _enum = None
                if 'enum' in _prop:
                    _enum = _prop['enum']
                
                _format = None
                if 'format' in _prop:
                    _format = _prop['format']
                if _type['type'] == list and 'items' in _prop and isinstance(_prop['items'], list):
                    _format = _prop['items'][0]['format']
                
                prop = {
                    '_name': _prop_name,
                    '_type': _type,
                    '_default': _default,
                    '_enum': _enum,
                    '_format' : _format
                }
                model['properties'].append(prop)
        return model

    def type_parser(self, t):
        _type = None
        _subtype = None
        if 'type' in t:
            if t['type'] == 'array' and 'items' in t:
                _type = self.J2P_TYPES[t['type']]
                if isinstance(t['items'], list):
                    if 'type' in t['items'][0]:
                        _subtype = self.J2P_TYPES[t['items'][0]['type']]
                    elif '$ref' in t['items'][0] or 'oneOf' in t['items'][0] and len(t['items'][0]['oneOf']) == 1:
                        if '$ref' in t['items'][0]:
                            ref = t['items'][0]['$ref']
                        else:
                            ref = t['items'][0]['oneOf'][0]['$ref']
                        _subtype = ref.split('/')[-1]
                elif isinstance(t['items'], dict):
                    if 'type' in t['items']:
                        _subtype = self.J2P_TYPES[t['items']['type']]
                    elif '$ref' in t['items'] or 'oneOf' in t['items'] and len(t['items']['oneOf']) == 1:
                        if '$ref' in t['items']:
                            ref = t['items']['$ref']
                        else:
                            ref = t['items']['oneOf'][0]['$ref']
                        _subtype = ref.split('/')[-1]
            elif isinstance(t['type'], list):
                _type = self.J2P_TYPES[t['type'][0]]
            elif t['type']:
                _type = self.J2P_TYPES[t['type']]
        elif '$ref' in t:
            _type = t['$ref'].split('/')[-1]
        elif 'anyOf' in t or  'allOf' in t or  'oneOf' in t:
            _type = list
        return { 'type': _type, 'subtype': _subtype }

    def write_file(self, filename):
        self.jinja.get_template(self.CLASS_TEMPLATE_FNAME).stream(models=self.definitions).dump(filename)

class readable_dir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir=values
        if not os.path.isdir(prospective_dir):
            raise argparse.ArgumentTypeError("readable_dir:{} is not a valid path".format(prospective_dir))
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace, self.dest, prospective_dir)
        else:
            raise argparse.ArgumentTypeError("readable_dir:{} is not a readable dir".format(prospective_dir))

def init_parser():
    parser = argparse.ArgumentParser(description="Converts JSON Schema to Plain Old Python Object")
    parser.add_argument('json_schema_file', type=argparse.FileType('r', encoding='utf-8'), help="Path to JSON Schema file to load")
    parser.add_argument('-t', '--templates-folder', action=readable_dir, help="Path to templates folder", default=JsonSchema2Popo.TEMPLATES_FOLDER)
    parser.add_argument('-o', '--output-file', type=argparse.FileType('w', encoding='utf-8'), help="Path to file output", default="model.py")
    return parser

if __name__ == '__main__':
    parser = init_parser()
    args = parser.parse_args()

    loader = JsonSchema2Popo()
    loader.load(args.json_schema_file)

    outfile = args.output_file
    loader.write_file(outfile)
