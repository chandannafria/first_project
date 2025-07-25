from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str)-> List[str]:
    '''
    this is function will return the list of requiremets
    '''
    requiremnts=[]
    
    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requiremnts=[req.replace('\n',"") for req in requiremnts ]
        
        if HYPEN_E_DOT in requiremnts:
            requiremnts.remove(HYPEN_E_DOT)
        
        return requiremnts


setup(
    name='mlproject',
    version='0.0.1',
    author='chandan',
    author_email= 'chandannafria@gmail.com',
    packages=find_packages(),
    install_require= get_requirements('requirements.txt')

)