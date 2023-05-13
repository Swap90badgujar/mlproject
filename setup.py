from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> list[str]:
    """Get requirements from file."""
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    author='swapnil',
    author_email = 'swapnilbadgujar59@gmail.com', 
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)
