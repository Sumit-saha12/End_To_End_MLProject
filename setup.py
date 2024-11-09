from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'

def get_package(file_path:str) -> list[str]:
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='End To End Machine Learning',
    version='0.0.1',
    description='Practising Data Science project, End to End implementation',
    author='Sumit',
    author_email='sumit.saha12072000@gmail.com',
    packages=find_packages(),
    requires=get_package('requirements.txt')
)