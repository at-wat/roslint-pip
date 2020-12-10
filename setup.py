from setuptools import setup, find_packages

setup(
    name='roslint-pip',
    version='0.11.2',
    description='pip roslint',
    url='https://github.com/at-wat/roslint-pip',
    author='anonymous',
    author_email='anonymous@foo',
    package_dir={'': 'src'},
    packages=['roslint'],
    entry_points={
        'console_scripts': [
            'roslint-cpplint = roslint.roslint_cpplint:main',
            'roslint-pep8 = roslint.roslint_pep8:main'
        ]
    },
    license="BSD"
)
