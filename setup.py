#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

description = "sisyphuswxg-toolbox"
version = "1.0.0"

setup(
    name="sisyphuswxg-toolbox",
    version=version,
    author="Wang Xuguang",
    author_email="sisyphuswxg@gmail.com",
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    keywords="sisyphuswxg-toolbox",
    url="...",
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 "Programming Language :: Python",
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    platforms='any',
    include_package_data=True,
    package_data={"": ["*.md"]},
    package_dir={"": "sisyphuswxg"},
    entry_points={"console_scripts": ["sisyphuswxg = sisyphuswxg:main"]},
    setup_requires=["wheel"],
    scripts=['sisyphuswxg/sisyphuswxg.py']
)
