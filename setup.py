from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='IJO',
    description='python package for sorting',
    long_description=open('README.md').read(),
    install_requires= ['numpy'],
    url='https://github.com/Dapo-Oke',
    author='Ifedapo Oke',
    author_email='ifedapo.john@gmail.com'
)