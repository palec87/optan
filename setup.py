import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='optan',
    author='David Palecek',
    author_email='david@stanka.de',
    description='Testing optan package',
    keywords='optan, test',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/palec87/optan',
    # project_urls={
    #     'Documentation': 'https://github.com/tomchen/example_pypi_package',
    #     'Bug Reports':
    #     'https://github.com/tomchen/example_pypi_package/issues',
    #     'Source Code': 'https://github.com/tomchen/example_pypi_package',
    #     # 'Funding': '',
    #     # 'Say Thanks!': '',
    # },
    package_dir={'': 'optan'},
    packages=setuptools.find_packages(where='optan'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    # install_requires=['Pillow'],
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