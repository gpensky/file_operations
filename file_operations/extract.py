from file_operations.pdf import pdf2str
from file_operations.office import doc2str
from file_operations.image import image2str
from file_operations.audio import audio2str


# File -> Python Object
# -----------------------------------------------------------------------------


def text_extract(file_path: str) -> str:
    """Extracts the text from a non-pure-text file independent of file type

    Args:
        file_path (str): file path
        output_path (str): output path
    """

    # AUDIO
    if file_path.lower().endswith((".mp3", ".mp4", ".wav", ".ogg")):
        return audio2str(file_path)
    # IMAGE
    elif file_path.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".gif", ".bmp")):
        return image2str(file_path)
    # PDF
    elif file_path.lower().endswith(".pdf"):
        return pdf2str(file_path)
    # DOC
    elif file_path.lower().endswith((".doc", ".docx", ".xls", ".xlsx")):
        return doc2str(file_path)
    else:
        return ""
        
