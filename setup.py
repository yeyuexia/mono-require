# coding: utf8

from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="mono-require",
    version="0.01",
    description="lock the file when access local resource",
    log_description=long_description,
    url="https://github.com/yeyuexia/mono-require",
    author="yeyuexia",
    author_email="yyxworld@gmail.com",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    keywords='lock when access local file'
)
