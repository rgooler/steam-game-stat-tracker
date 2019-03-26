#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2017 FireEye, Inc. All Rights Reserved.

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


requirements = [
    "requests"
]

# this sets __version__
# via: http://stackoverflow.com/a/7071358/87207
# and: http://stackoverflow.com/a/2073599/87207
with open(os.path.join("steamgamestattracker", "version.py"), "rb") as f:
    exec(f.read())

setup(
    name='steamgamestattracker',
    version=__version__, # pylint:disable=undefined-variable
    description="",
    long_description="",
    author="Ryan Gooler",
    author_email='ryan.gooler@gmail.com',
    url='https://www.github.com/rgooler/steam-game-stat-tracker',
    packages=[
        'steamgamestattracker',
    ],
    package_dir={'steamgamestattracker': 'steamgamestattracker'},
    entry_points={
        "console_scripts": [
            "steamgamestattracker=steamgamestattracker.main:main",
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='steam',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
    ],
)