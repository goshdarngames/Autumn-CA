"""A setuptools based setup module for Autumn-CA"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

from setuptools.extension import Extension
from Cython.Build import cythonize

import versioneer

import numpy

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'numpy',
    'cython'
]

test_requirements = [
    'numpy',
    'cython'
]

#Cython classes
extensions = [
   Extension(
      "autumn_ca.cellular_automata.neighbourhood",
      [
         "autumn_ca/cellular_automata/neighbourhood.pyx"
      ],
      include_dirs=[numpy.get_include ()]
   )
]

setup(
    name='Autumn-CA',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Cellular Automata.",
    long_description=readme + '\n\n' + history,
    author="Gosh Darn Games",
    author_email='none',
    url='https://github.com/goshdarngames/autumn-ca',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts':[
            'autumn-ca=autumn_ca.cli:cli',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,

    ext_modules = cythonize(extensions)
)
