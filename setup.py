#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    "jinja2",
    "jingo",
]

setup(
    name="jutils",
    version="0.1",
    author="Donald Stufft",
    author_email="donald.stufft@gmail.com",
    url="https://github.com/dstufft/jutils",
    description="A collection of jingo helpers for various purposes.",
    license=open("LICENSE").read(),
    packages=find_packages(exclude=("tests",)),
    package_data={'': ["LICENSE"]},
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
    ],
)
