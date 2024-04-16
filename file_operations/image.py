"""audio.py - This module provides functions to read/write audio files."""

from PIL import Image
import pytesseract


def image2str(image_path: str, lang: str = "por") -> str:
    """Read text from images

    Args:
        image_path (str): image file path

    Returns:
        str: text from image
    """

    # Read the image
    img = Image.open(image_path)
    # Extract the text from the image
    try:
        text = pytesseract.image_to_string(img, lang=lang, timeout=300)
    except RuntimeError:
        return ""
    return text
