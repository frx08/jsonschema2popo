from setuptools import setup
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="jsonschema2popo",
    version=find_version("jsonschema2popo", "__init__.py"),
    description="Converts a JSON Schema to a Plain Old Python Object class",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    url="https://github.com/frx08/jsonschema2popo",
    author="cruc.io",
    author_email="frx089@gmail.com",
    keywords="python json-schema code-generator",
    license="MIT License",
    python_requires=">=3.4",
    install_requires=["Jinja2>=2.10", "networkx==1.9"],
    packages=["jsonschema2popo"],
    package_data={"jsonschema2popo": ["_class.tmpl"]},
    include_package_data=True,
    entry_points={
        "console_scripts": ["jsonschema2popo=jsonschema2popo.jsonschema2popo:main"]
    },
)
