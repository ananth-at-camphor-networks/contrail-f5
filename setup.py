#
# Copyright (c) 2014 Juniper Networks, Inc. All rights reserved.
#

from setuptools import setup, find_packages
import glob, os

def get_files(source, target):
    files = filter(lambda x: '__init__.py' not in x, glob.glob(source+'/*'))
    return (target, files)

def requirements(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

setup(
    name='contrail_f5',
    version='0.1dev',
    packages=find_packages(),
    zip_safe=False,
    long_description="F5 loadbalancer bigip_interfaces",
    install_requires=requirements('requirements.txt'),
)
