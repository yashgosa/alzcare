from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) ->List[str]:
    """Get requirements from requirements.txt file."""

    # Initalise requirements list
    requirements = []

    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements

setup(
    name = "alzcare",
    version = "0.0.1",
    author="Yash Chandrakant Gosavi",
    author_email="yashcgosavi@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)