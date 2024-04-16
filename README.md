# file-operations

Collection of multiple file operation functions. The goal here is to facilitate the use and convertion of multiple file types for machine learning applications.

Currently this package supports:

- audio: transcription using whisper
- csv
- dir: directory operations
- image: text extraction using tesseract
- json
- office: text extraction
- pdf: text extraction including OCR with tesseract
- text
- xml
- zip

## Table of Contents

- [file-operations](#file-operations)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Dependencies](#dependencies)
    - [tesseract](#tesseract)
    - [pdf2image](#pdf2image)
    - [antiword](#antiword)
    - [FFMPEG](#ffmpeg)
  - [Usage](#usage)
  - [Contributing](#contributing)

## Installation

To install python package:

```pip install git+https://github.com/gpensky/file-operations.git```

## Dependencies

### tesseract

The ``.pdf`` extraction depends on the ``tesseract`` software to perform OCR on images.

**Windows**:

> For Windows users, you can follow these steps to install the [link](https://linuxhint.com/install-tesseract-windows/). Then, when you download and install the software, you need to add their executable paths to Environment Variables on your computer. Alternatively, you can run the following commands to directly include their paths in the Python script using the following code:
>
> ```pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe```
>
> [Source](https://towardsdatascience.com/extracting-text-from-pdf-files-with-python-a-comprehensive-guide-9fc4003d517)

**Linux**:

```sudo apt install tesseract-ocr```

### pdf2image

The ``.pdf`` extraction depends on the ``poppler`` software to perform the conversion of ``.pdf`` files to images.

**Windows**:

> Windows users will have to build or download poppler for Windows. I recommend [@oschwartz10612](https://github.com/oschwartz10612/poppler-windows/releases/) version which is the most up-to-date. You will then have to add the bin/ folder to [PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) or use ``poppler_path = r"C:\path\to\poppler-xx\bin"`` as an argument in ``convert_from_path``.
>
> [Source](https://github.com/Belval/pdf2image)

**Linux**:

```sudo apt-get install -y poppler-utils```

### antiword

The Word files extraction depends on the ``antiword`` software to extract text from ``.doc`` files.

**Windows**:

> - Download antiword from [here](http://www.softpedia.com/get/Office-tools/Other-Office-Tools/Antiword.shtml)
> - Extract the antiword ``.zip``
> - The Windows version looks for its mapping files in %HOME%\antiword if HOME is set and in C:\antiword if HOME is not set.
> - Add the path antiword folder to your PATH environment variable.
>
> Source 1: 00README.WIN on antiword folder
>
> [Source 2](https://stackoverflow.com/questions/51727237/reading-doc-file-in-python-using-antiword-in-windows-also-docx)

**Linux**:

```sudo apt-get install -y antiword```

### FFMPEG

To transcribe audio files, ``whisper`` uses ``FFMPEG``.

**Windows**:

- Download from [FFMPEG](https://ffmpeg.org/download.html)
- Move ``.exe`` to any folder and add to PATH.

**Linux**:

```sudo apt-get install -y ffmpeg```

## Usage

To use, just include the package and call a function. Example:

```python
from file-operations.audio import audio2str

transcription = audio2str(file_path)
```

## Contributing

Some implementation are still missing:

- implement extract functions
- implement extract test
- add more office functions
- implement office tests
- implement pdf tests
- implement xml tests
- implement zip tests
- write documentation
