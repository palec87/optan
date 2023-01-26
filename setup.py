#!/usr/bin/env python3

import setuptools
from pathlib import Path

project_dir = Path(__file__).parent

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

requires = [
    'numpy>=1.23',
    'matplotlib>=3.2',
    'pandas',
    'scipy',
]

setuptools.setup(
    name='optan',
    version="0.0.0",
    author='David Palecek',
    author_email='david@stanka.de',
    description='OPT processing for OPTac data',
    keywords='optan, test',
    long_description=project_dir.joinpath("README.md").read_text(encoding="utf-8"),,
    long_description_content_type='text/markdown',
    url='https://github.com/palec87/optan',
    # project_urls={
    #     'Documentation': 'https://github.com/tomchen/example_pypi_package',
    #     'Bug Reports':
    #     'https://github.com/tomchen/example_pypi_package/issues',
        # 'Source Code': 'https://github.com/palec87/optan',
    #     # 'Funding': '',
    #     # 'Say Thanks!': '',
    # },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Image Processing',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=project_dir.joinpath("requirements.txt").read_text().split("\n"),
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)