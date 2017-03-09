from setuptools import setup

setup(
    name='Empty',
    version='0.2',
    license='BSD',
    url='https://github.com/italomaia/empty',
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
