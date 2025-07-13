# Copyright (c) Facebook, Inc. and its affiliates
# Copyright (c) Rutav Shah, Indian Institute of Technlogy Kharagpur

import os
import sys
from setuptools import setup, find_packages

print("Installing RRL-dependencies. \n Package intended for use with provided conda env. See setup instructions here:")

if sys.version_info.major != 3:
    print("This Python is only compatible with Python 3, but you are running "
          "Python {}. The installation will likely fail.".format(sys.version_info.major))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='RRL-dependencies',
    version='1.0.0',
    packages=find_packages() + find_packages(where='mjrl') + find_packages(where='mj_envs'),
    package_dir={
        '': '.',
        'mjrl': 'mjrl/mjrl',
        'mj_envs': 'mj_envs/mj_envs',
    },
    description='RL algorithm for environments in MuJoCo',
    author='Rutav Shah (Modified by Youngdo Lee)',
    author_email='lyd0531@kaist.ac.kr',
    install_requires=[
        'click',
        'termcolor',
    ],
    include_package_data=True,
    zip_safe=False,
)