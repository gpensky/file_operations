# extract

## Introduction

extract is responsible for extracting multiple file types to text or to a folder with the files, as described below.

## Supported files

| File Input | File Output              |
| ---------- | ------------------------ |
| ``.doc``   | ``.txt``                 |
| ``.docx``  | ``.txt``                 |
| ``.xls``   | ``.txt``                 |
| ``.xlsx``  | ``.txt``                 |
| ``.pdf``   | ``.txt``                 |
| ``.jpeg``  | ``.txt``                 |
| ``.png``   | ``.txt``                 |
| ``.mp3``   | ``.txt``                 |
| ``.zip``   | folder with all files    |

## Details on the extraction scripts

### ``.pdf`` extraction

The ``.pdf`` text extraction is based on this [python notebook](https://github.com/g-stavrakis/PDF_Text_Extraction/blob/main/PDF_Reader.ipynb) and explaned in details in this [article](https://towardsdatascience.com/extracting-text-from-pdf-files-with-python-a-comprehensive-guide-9fc4003d517).
Minimum adjustments were made to the original script, just to provide an external interface for the main function.

### Image extraction

Text extraction from images is performed using `tesseract`, and is part of the ``.pdf`` extraction, described above.

### Word files extraction

The ``.doc``, ``.docx``, ``xls`` and ``.xlsx`` text extraction is made using [``textract``](https://textract.readthedocs.io/). There are more details on the documentation.

### Audio extraction

Audio transcription is made using ``whisper``. External dependencies and instalation procedure for Windows is described in this [article](https://github.com/openai/whisper/discussions/1463).
