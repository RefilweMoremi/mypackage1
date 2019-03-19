from setuptools import setup, find_packages

setup(
    name='mypackage1',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Recursion and sorting python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/RefilweMoremi/mypackage1',
    author='Refilwe',
    author_email='refilwe.moremi12@gmail.com'
)
