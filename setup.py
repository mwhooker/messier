#!/usr/bin/env python

import sys

from setuptools import setup, find_packages


with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

if sys.version_info < (2, 7):
    install_requires.append("argparse")

version = "0.1.0"

setup(
    name="messier",
    version=version,
    description="Messier, a dashboard for AWS",
    long_description="Messier, a dashboard for AWS",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Topic :: System :: Installation/Setup"
    ],
    keywords="",
    author="Scott Smith",
    author_email="scott@ohlol.net",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "messier = messier.cli:main"
        ],
    }
)
