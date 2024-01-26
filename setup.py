#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name="mdx-escape-html",
    version="0.1",
    description="Python-markdown extension to escape HTML in raw markdown.",
    long_description="",
    author="Noemi Millman",
    author_email="noemi@triopter.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["markdown"],
    extras_require={"dev": ["pytest"]},
    license="MIT",
    zip_safe=False,
)
