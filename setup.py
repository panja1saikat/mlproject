from setuptools import find_packages, setup
from typing import List


HYPER_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:

### This list will returns the requirements
 requirements=[]
 with open(file_path) as file_obj:
    requirement=file_obj.readline()
    requirements=[req.replace("\n"," ") for req in requirements]

    if HYPER_E_DOT in requirements:
        requirements.remove(HYPER_E_DOT)

 return requirement




setup(

 name="mlproject",
 version='0.0.1',
 author="saikat",
 author_email= "saikatpanja.udemy@gmail.com",
 packages= find_packages(),
 install_requies=get_requirements('requirements.txt')

)