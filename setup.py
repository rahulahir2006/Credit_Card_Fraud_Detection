from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path)->List[str]:
    '''
    Read requirements from a file and return a list of requirements.
    '''
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[req.replace('\n',' ') for req in requirements if not req.startswith('#')]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    name='CreditCardFraudDetection',
    version='0.1.0',

    authors='Rahul Zaru',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)