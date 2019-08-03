from setuptools import setup, find_packages

setup(
    name='calculator',
    version='0.1.0',
    url='',
    license='MIT',
    author='aliaksandr kakhanovich',
    author_email='kakhanovichal@gmail.com',
    description='simple calculator',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pycalc = calculator.pycalc:main',
        ]
    }
)
