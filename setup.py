#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from petl_django import __version__ as version

long_description = 'Please see the documentation at the `project page <https://github.com/PGower/petl_django>`_ .'

packages = [
    'petl_django',
]

package_data = {
    '': ['LICENSE', 'README.md'],
}

setup(
    name='petl_django',
    version=version,
    description='A petl view class for django model data.',
    long_description=long_description,
    author='Paul Gower',
    author_email='p.gower@gmail.com',
    url='https://github.com/PGower/petl_django',
    download_url='https://github.com/PGower/petl_django/releases',
    package_dir={'petl_django': 'petl_django'},
    packages=packages,
    package_data=package_data,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['petl', 'django'],
    install_requires=['petl', 'django'],
)
