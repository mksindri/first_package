
import codecs

from setuptools import setup

from os import path


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="first_package", # Replace with your own username
    version="0.0.1",
    author="Mukesh Kumar",
    author_email="mksindri@gmail.com",
    description="A small example package",
    long_description=long_description,
    url="https://github.com/mksindri/first_package",
    packages=setuptools.find_packages(),
    long_description_content_type='text/markdown',
)