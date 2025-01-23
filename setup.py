from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup


with open('README.rst') as fobj:
    long_description = fobj.read()


with open('version.txt') as fobj:
    version = fobj.read()


setup(
    name='django-user-language-middleware',
    version=version,
    author='Laura Barluzzi',
    author_email='laura@koalacoder.com',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/laura-barluzzi/django-user-language-middleware',
    download_url='https://pypi.python.org/pypi/django-user-language-middleware',
    license='Apache Software License',
    description='Django middleware to translate with language in user model',
    long_description=long_description,
    install_requires=[
        'Django>=3.2'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization'
    ])
