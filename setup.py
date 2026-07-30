from setuptools import setup

setup(
    name='options',
    version='0.1.0',
    packages=['options'],
    install_requires=[
        'click>=8.1.3',
        'tomli >= 1.1.0 ; python_version < "3.11"',
        'plotext>=5.2.7',
        'numpy>=1.23.4',
    ],
    entry_points={
        'console_scripts': [
            'options = options.main:cli',
        ],
    },
)
