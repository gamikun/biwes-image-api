#!/usr/bin/env python

import os
import sys

import biwesimg

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    sys.exit(os.system('python setup.py sdist upload'))

packages = [
    'biwesimg'
]

requires = ['requests', 'simplejson']

setup(
    name='biwesimg',
    version=biwesimg.__version__,
    description='biwes image converter implementation',
    long_description=open('changelog.txt').read(),
    author='Gamaliel Espinoza',
    author_email='gamaliel.espinoza@gmail.com',
    url='https://github.com/gamikun/biwes-image-api',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'biwesimg': ['*.pem']},
    package_dir={'biwesimg': 'biwesimg'},
    include_package_data=True,
    install_requires=requires,
    # license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',

    ),
)