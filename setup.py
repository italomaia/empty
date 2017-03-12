#!/usr/bin/env python
"""
Empty is a light wrapper around Flask which adds some
sensitive defaults to your project out of the box.

"""
from setuptools import setup
import empty

setup(
    name='Empty',
    version=empty.__version__,
    license='BSD',
    url='https://github.com/italomaia/empty',
    author='Italo Maia',
    description='Wrapper which makes Flask development easier',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    packages=['empty'],
    install_requires=[
        'Flask>=0.10'
    ],
    test_suite='runtests.suite',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
