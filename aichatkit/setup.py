import os
from setuptools import setup, find_packages


directory = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(directory, "requirements.txt"), "r") as file:
    requirements = file.read().splitlines()

setup(
    name="aichatkit",
    version="0.0.1",
    description="A comprehensive Python library for integrating AI-powered chat functionalities.",
    packages=find_packages(),
    install_requires=requirements
)
