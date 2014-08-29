from setuptools import setup
import os.path
import re

dirname = os.path.dirname(__file__)


def resolve_path(path):
    return os.path.join(dirname, path)


def read_lines(path):
    with open(resolve_path(path)) as f:
        return f.readlines()


def read(path):
    with open(resolve_path(path)) as f:
        return f.read()


def long_description():
    return re.split('\n\.\. pypi [^\n]*\n', read('README.rst'), 1)[1]


setup(
    name='chain_bitcoin',
    version='0.1',
    author='Chris Martin',
    author_email='ch.martin@gmail.com',
    packages=['chain_bitcoin'],
    data_files=[
        ('.', ['README.rst',
               'requirements-install.txt',
               'requirements-test.txt']),
    ],
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
