"""audio.py - This module provides functions to read/write audio files."""

from typing import Union
import whisper

# File -> Python Object
# -----------------------------------------------------------------------------


def audio2str(file_path: str, language: Union[str, None] = None, model_name: str = "tiny") -> str:
    """Transcribes audio and returns only the text. Uses `whisper` to transcribe: see
    [documentation](https://github.com/openai/whisper).

    Args:
        file_path (str): file path of audio file
        language (str, optional): audio language, if None will use auto language identificaiton.
        Defaults to None.

    Returns:
        str: text
    """

    return audio2dict(file_path, language, model_name)["text"]


def audio2dict(
    file_path: str, language: Union[str, None] = None, model_name: str = "tiny"
) -> dict:
    """Transcribe audio and returns the dict with information. Uses `whisper` to transcribe: see
    [documentation](https://github.com/openai/whisper).

    Args:
        file_path (str): file path of audio file
        language (str, optional): audio language, if None will use auto language identificaiton.
        Defaults to None.
        model_name (str, optional): model name, can be 'tiny', 'base', 'small', 'medium' or
        'large'. Defaults to 'large'.

    Returns:
        dict: A dictionary containing the resulting text ("text") and segment-level details
        ("segments"), and the spoken language ("language").
    """

    model = whisper.load_model(model_name)

    if language is not None:
        result = model.transcribe(file_path, language=language, verbose=False)
    else:
        result = model.transcribe(file_path, verbose=False)

    return result
