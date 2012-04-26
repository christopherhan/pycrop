import os
from setuptools import setup

setup(
    name='pycrop',
    version='1.0',
    author="CondeNet, Inc / Chris Han",
    description="Smart image cropping for Python. Modified reddit's image cropping algorithm to produce square thumbnails.",
    url='https://github.com/christopherhan/pycrop',
    classifiers = [
        'Development Status :: Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = [
        'PIL',
    ],
)
