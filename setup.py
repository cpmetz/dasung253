#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='dasung',
      version='1.0',
      # Modules to import from other scripts:
      packages=find_packages(),
      # Executables
      scripts=["dasung.py"],
     )
