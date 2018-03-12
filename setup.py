from pip.req import parse_requirements
from setuptools import setup
import uuid

setup(
        name='jsonschema2popo',
        version='0.1',
        modules=['jsonschema2popo'],
        scripts=['jsonschema2popo.py'],
        url='https://github.com/frx08/jsonschema2popo',
        license='MIT License',
        author='cruc.io',
        author_email='',
        description='Converts a JSON Schema to a Plain Old Python Object class',
        install_requires= [str(ir.req) for ir in parse_requirements('requirements.txt', session=uuid.uuid1())]
)