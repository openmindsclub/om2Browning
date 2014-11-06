#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tornado systemd - Use socket activation with tornado
"""
import os
import re
from setuptools import setup

ROOT = os.path.dirname(__file__)
with open(os.path.join(ROOT, 'tornado_systemd', '__init__.py')) as fd:
    __version__ = re.search("__version__ = '([^']+)'", fd.read()).group(1)

options = dict(
    name="tornado_systemd",
    version=__version__,
    description="Use socket activation with tornado",
    long_description="See http://github.com/paradoxxxzero/tornado_systemd",
    author="Florian Mounier",
    author_email="paradoxxx.zero@gmail.com",
    url="http://github.com/paradoxxxzero/tornado_systemd",
    license="GPLv3",
    packages=['tornado_systemd'],
    platforms="Any",
    install_requires=["tornado>=3.2"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"])

setup(**options)
