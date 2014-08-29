from setuptools import setup
import pkg_resources
import re


def read(path):
    with open(pkg_resources.resource_filename(__name__, path)) as f:
        return f.read()


def long_description():
    return re.split('\n\.\. pypi [^\n]*\n', read('README.rst'), 1)[1]


setup(
    name='chain_bitcoin',
    version='0.4',
    author='Chris Martin',
    author_email='ch.martin@gmail.com',
    packages=['chain_bitcoin'],
    package_data={'chain_bitcoin': ['chain.pem']},
    include_package_data=True,
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
    install_requires=read('requirements-install.txt').split('\n'),
    tests_require=read('requirements-test.txt').split('\n'),
)
