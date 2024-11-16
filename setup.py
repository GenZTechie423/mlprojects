# This is responsible for converting the ML application to a package
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."  # this variable is mapped to setup.pypip


def get_requirements(file_path: str) -> list[str]:
    """
    this function will return the list of requirements
    """

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mlprojects",
    version="0.1",
    author="Sudd",
    author_email="genztechie950@gmail.com",
    packages=find_packages(),
    install_requires=["pandas", "numpy", "seaborn"],
)
