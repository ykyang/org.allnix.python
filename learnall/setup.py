from setuptools import setup

setup(
    name='learnall',
    version='0.1.0',
    author='Yi-Kun Yang',
    author_email='ykyang@gmail.com',
    packages=['learnall'], #, 'package_name.test'],
    license='LICENSE',
    description='A package to learn Python',
    install_requires=[
        'flask',
        'matplotlib',
        'pyside2',
        'qt',
        'qtawesome',
        'vtk',
    ]
)