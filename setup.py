from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup


with open('README.rst') as fobj:
    long_description = fobj.read()


setup(
    name='django-user-language-middleware',
    version='0.0.1',
    author='Laura Barluzzi',
    author_email='laura@koalacoder.com',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/laura-barluzzi/django-user-language-middleware',
    download_url='https://pypi.python.org/pypi/django-user-language-middleware',
    license='Apache Software License',
    description='Django middleware to translate with language in user model',
    long_description=long_description,
    install_requires=[
        'Django>=1.8'
    ],
    python_requires='==2.7,==3.6',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization'
    ])