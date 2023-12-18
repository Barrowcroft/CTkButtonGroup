import os

from setuptools import setup


def read(fname: str):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ctkbuttongroup",
    version="1.0.0",
    author="Barrowcroft",
    author_email="barrowcroft@outlook.com",
    description=(
        "Four simple classes to facilitate the creation of groups of buttons, check boxes, radio buttons and switches."
    ),
    license="MIT",
    keywords="customtkinter button group",
    url="https://github.com/Barrowcroft/CtkButtonGroup.git",
    packages=["ctkbuttongroup"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "customtkinter >= 5.2.1",
        "darkdetect >= 0.8.0",
        "packaging >= 23.2",
    ],
    python_requires=">=3.12",
)
