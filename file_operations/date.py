from dateutil.parser import parse
from dateutil.parser._parser import ParserError


# Date String -> Date String
# -----------------------------------------------------------------------------


def br2iso(date_str: str) -> str:
    """Convert brazilian date format string (DD/MM/YYYY) to ISO date format string (YYYY-MM-DD)

    Args:
        date_str (str): brazilian date format string

    Returns:
        str: ISO date format string
    """
    try:
        return parse(date_str, dayfirst=True).date().strftime("%Y-%m-%d")
    except ParserError:
        return ""


def iso2br(date_str: str) -> str:
    """Convert ISO date format string (YYYY-MM-DD) to brazilian date format string (DD/MM/YYYY)

    Args:
        date_str (str): ISO date format string

    Returns:
        str: brazilian date format string
    """
    try:
        return parse(date_str).date().strftime("%d/%m/%Y")
    except ParserError:
        return ""
