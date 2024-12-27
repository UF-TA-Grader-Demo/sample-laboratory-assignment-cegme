from setuptools import setup, find_packages

setup(
    name='data_exploration_wrangling',
    version='1.0',
    author='Christan Grant',
    author_email='christan@ufl.edu',
    packages=find_packages(exclude=('tests', 'docs', 'resources')),
    install_requires=[
        'pandas',
        'matplotlib',
        'numpy'
    ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'data_wrangling=data_wrangling.main:main'
        ]
    }
)
