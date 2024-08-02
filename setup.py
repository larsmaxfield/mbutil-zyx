from setuptools import setup

setup(
    name='mbutil_zyx',
    version='0.4.0',
    author='Lars Maxfield',
    author_email='null',
    packages=['mbutil_zyx'],
    scripts=['mb-util-zyx'],
    url='https://github.com/larsmaxfield/mbutil_zyx',
    license='LICENSE.md',
    description='An importer and exporter for MBTiles with the zyx scheme',
    long_description=open('README.md').read(),
)
