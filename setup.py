import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="slack-blocks-wrapper",
    version="0.2.6",
    description="A python3 wrapper for the slack block kit framework",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AllanPy/slack-blocks-wrapper",
    author="Allan Mogusu",
    author_email="allannelly690@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*", "examples"]
    ),
    include_package_data=True
)
