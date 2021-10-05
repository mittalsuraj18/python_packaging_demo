from setuptools import setup, find_packages

setup(
    name = "my_package",
    version = "0.1" , 
    packages=find_packages(),
    license = "No License",
    author="suraj.mittal",
    install_requires = ["pandas"]
)


setup(
    name="my_packages_2",
    packages=find_packages(where="src"),
    version="0.1",
    description="pacakging inside src folder",
    author="suraj.mittal",
    package_dir={"": "src"},
)
