from setuptools import setup,setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='MiPyBand2',
    version='0.0.1',
    description='Library to work with Xiaomi MiBand 2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DavidM42/MiBand2',
    author='DavidM42',
    author_email='david@merz.dev',
    license='CC0 1.0 Universal',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'bluepy==1.3.0',
        'pycrypto==2.6.1',
    ])