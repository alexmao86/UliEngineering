#!/usr/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup

setup(name='UliEngineering',
      version='0.1',
      description='Computational tools for electronics engineering',
      author='Uli Köhler',
      author_email='ukoehler@techoverflow.net',
      url='http://techoverflow.net/',
      packages=['UliEngineering'],
      requires=['numpy (>= 1.5)'],
      test_suite="tests",
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Information Analysis'
      ]
     )
