from distutils.core import setup
from setuptools import find_packages

setup(
    name='image_augmentor',
    packages = ['image_augmentor'],
    version='0.1.2',
    author='Michael Mendoza',
    author_email='iammichaelmendoza@gmail.com',
    scripts=[],
    url='https://github.com/michaelmendoza/image_augmentor',
    license='GPL',
    description='An image augmentation library for machine learning',
    long_description=open('README.rst').read(),
    install_requires=[
        "numpy==1.14.1",
        "scipy==1.0.0",
        "matplotlib==2.1.1",
        "tqdm==4.19.9"
    ],
    python_requires='>=2.7',
)