from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext
import sys
import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="hypixel-skyblock-utility",
    version="0.1.0",
    author="khouneeshraut",
    description="Production-ready Hypixel SkyBlock utility with autoclicker, macros, and market analyzer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khouneeshraut/hypixel-skyblock-utility",
    packages=find_packages(where="src/python"),
    package_dir={"": "src/python"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "hypixel-utility=main:main",
        ],
    },
)
