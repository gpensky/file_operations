"""Setup"""

from setuptools import setup, find_packages

setup(
    name="file_operations",
    version="0.2.0",
    author="Gabriel Pensky",
    author_email="gabriel.pensky@gmail.com",
    description="Collection of multiple file operation functions with the goal of facilitating the use and convertion of multiple file types for machine learning applications.",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gpensky/file-operations",
    packages=find_packages(),
    install_requires=[
        "openai-whisper @ git+https://git@github.com/openai/whisper.git#egg=openai-whisper",
        "pandas==1.3.4",
        "textract==1.5.0",
        "xmltodict==0.13.0",
        "PyPDF2==3.0.1",
        "pdfminer",
        "pdfplumber==0.10.3",
        "pdf2image==1.17.0",
        "pytesseract==0.3.10",
    ],
    python_requires=">=3.9",
)
