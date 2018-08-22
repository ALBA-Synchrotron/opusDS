#!/usr/bin/env python

from setuptools import setup, find_packages

# The version is updated automatically with bumpversion
# Do not update manually
__version = '0.4.0-alpha'

long_description = """This is a Windows socket server to manipulate the OPUS
Spectroscopy Software (BRUKER).
"""


classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='opusServer',
    version=__version,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['opusServer = opusServer.opusserver:run_opus_server']
    }, # METADATA
    author='Carlos Falcon',
    author_email='cfalcon@cells.es',
    include_package_data=True,
    license='LGPL',
    description='Opus Socket Server',
    long_description=long_description,
    requires=['setuptools (>=1.1)'],
    classifiers=classifiers
)
