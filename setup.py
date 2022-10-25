from setuptools import setup

setup(
    name='options',
    version='0.1.0',
    py_modules=['options'],
    install_requires=[
        'click==8.1.3',
        'datetime==4.7', 
        'tomli >= 1.1.0 ; python_version < "3.11"', 
    ],
    entry_points={
        'console_scripts': [
            'options = options.main:cli',
        ],
    },
)
