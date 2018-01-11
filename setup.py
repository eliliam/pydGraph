from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='pydgraph',  # Required
    version='0.1.0',  # Required
    description='A Python package to easily work with graphs',  # Required
    long_description=long_description,  # Optional
    url='github.com/eliliam/pydGraph',  # Optional
    author='Eli Smith',  # Optional
    author_email='eli.liam.smith@gmail.com',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Graphs',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='graphs networkx pathfinding',  # Optional
    py_module=['pydGraph'],  # Required
    install_requires=['networkx', 'matplotlib'],  # Optional
)