from distutils.core import setup

setup(
    name='chain_bitcoin',
    version='0.1',
    packages=['chain_bitcoin'],
    url='https://github.com/cardforcoin/chain-bitcoin-python',
    license='MIT',
    description='Integration library for the Chain.com API',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'requests>=2',
    ],
    tests_require=[
    ],
)
