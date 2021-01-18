
import codecs

from setuptools import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with codecs.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()



import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description_content_type='text/markdown',
)