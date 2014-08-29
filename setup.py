from setuptools import setup
import pkg_resources
import re

name = 'chain_bitcoin'


def open_resource(r):
    return open(pkg_resources.resource_filename(
        pkg_resources.Requirement.parse(name), r))


def read_lines(r):
    with open_resource(r) as f:
        return f.readlines()


def read(r):
    with open_resource(r) as f:
        return f.read()


def long_description():
    return re.split('\n\.\. pypi [^\n]*\n', read('README.rst'), 1)[1]


setup(
    name=name,
    version='0.1',
    author='Chris Martin',
    author_email='ch.martin@gmail.com',
    packages=['chain_bitcoin'],
    url='https://github.com/cardforcoin/chain-bitcoin-python',
    license='MIT',
    description='Integration library for the Chain.com API',
    long_description=long_description(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=read_lines('requirements-install.txt'),
    tests_require=read_lines('requirements-test.txt'),
)
