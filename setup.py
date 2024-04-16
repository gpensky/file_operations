"""Setup"""

from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open("requirements.txt", encoding="utf8") as f:
    required_packages = f.read().splitlines()

setup(
    name="file_operations",
    version="0.1.0",
    author="Gabriel Pensky",
    author_email="gabriel.pensky@gmail.com",
    description="Collection of multiple file operation functions with the goal of facilitating the use and convertion of multiple file types for machine learning applications.",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gpensky/file-operations",
    packages=find_packages(),
    install_requires=required_packages,
    python_requires=">=3.9",
)
