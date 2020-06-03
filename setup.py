#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='acunetix',
      version='1.0.0',
      description='Python library that provides access to the API of acunetix scanner',
      author='Hossam Mohamed, Ahmed M. Elhady',
      author_email='wazehell@outlook.com, amelhadyy@gmail.com',
      url='https://github.com/WazeHell/acunetix-python',
      packages=find_packages(),
      install_requires=[
          'requests'
      ],
)