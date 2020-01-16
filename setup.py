import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


setup(
    name="django-path-dbrouter",
    version="0.1.0",
    url="http://github.com/amsterdam",
    license="MIT",
    author="Jan Murre",
    author_email="jan.murre@catalyz.nl",
    description="Django DB Router based on request path.",
    long_description=read("README.rst"),
    packages=find_packages(exclude=("tests",)),
    install_requires=["dj_database_url"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
