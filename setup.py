from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.strip() for i in requirements if i.strip()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="NextJam",
    version="0.0.1",
    description="A package to find your next jam based on your mood",
    author="Bhavya Jha",
    author_email="bhavyajha1404@gmail.com",
    packages=find_packages(include=["nextjam", "nextjam.*"]),
    install_requires=get_requirements("requirements.txt"),
    include_package_data=True,
)
