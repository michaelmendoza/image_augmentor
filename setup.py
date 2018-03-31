from distutils.core import setup
from setuptools import find_packages

setup(
    name='image_augmentor',
    version='0.1.0',
    author='Michael Mendoza',
    author_email='iammichaelmendoza@gmail.com',
    scripts=[],
    url='https://github.com/michaelmendoza/image_augmentor',
    license='GPL',
    description='Augments an image set with randomly generated transformed images to increase the size of image dataset',
    long_description=open('README.rst').read(),
    install_requires=[
        "numpy==1.14.1",
        "scipy==1.0.0",
        "matplotlib==2.1.1",
        "tqdm==4.19.9"
    ],
    python_requires='>=2.7',
)