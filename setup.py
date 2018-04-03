from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='jsonschema2popo',
        version='0.8',
        description='Converts a JSON Schema to a Plain Old Python Object class',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/frx08/jsonschema2popo',
        author='cruc.io',
        author_email='frx089@gmail.com',
        keywords='python json-schema code-generator',
        license='MIT License',
        python_requires='>=3.4',
        scripts=['jsonschema2popo/jsonschema2popo.py'],
        packages=["jsonschema2popo"],
        package_data={"jsonschema2popo": ["_class.tmpl"]},
        include_package_data=True,
        entry_points={"console_scripts": ["jsonschema2popo = jsonschema2popo.jsonschema2popo:main"]},
)
