from setuptools import setup, find_packages

setup(
    name='roslint',
    version='0.11.2',
    description='pip roslint',
    url='https://github.com/at-wat/roslint-pip',
    author='anonymous',
    author_email='anonymous@foo',
    packages=find_packages(exclude=['tests', 'cmake']),
    entry_points={
        'console_scripts': [
            'roslint-cpplint = roslint.roslint_cpplint',
            'roslint-pep8 = roslint.roslint_pep8'
        ]
    },
    license="BSD"
)
