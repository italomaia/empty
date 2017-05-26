#!/usr/bin/env python
"""
Empty is a light wrapper around Flask which adds some
sensitive defaults to your project out of the box.

"""
from setuptools import setup


setup(
    name='empty',
    version='0.3.3',
    license='BSD',
    url='https://github.com/italomaia/empty',
    author='Italo Maia',
    description='Wrapper which makes Flask development easier',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    packages=['empty'],
    install_requires=['flask>=0.12.2'],
    test_suite='runtests.suite',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
