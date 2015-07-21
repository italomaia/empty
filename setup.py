from setuptools import setup

setup(
    name='Empty',
    version='0.1',
    license='BSD',
    author='Italo Moreira Campelo Maia',
    description='Wrapper which makes Flask development easier',
    platforms='any',
    packages=["empty"],
    install_requires=[
        'Flask>=0.10'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
