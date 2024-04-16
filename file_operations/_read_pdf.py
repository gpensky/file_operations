"""Script to read and extract text from pdf files.
Based on:
https://towardsdatascience.com/extracting-text-from-pdf-files-with-python-a-comprehensive-guide-9fc4003d517
https://github.com/g-stavrakis/PDF_Text_Extraction/blob/main/PDF_Reader.ipynb
"""

# To remove the additional created files
import os

# For type hints
from typing import Any

# To read the PDF
import PyPDF2

# To analyze the PDF layout and extract text
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTComponent, LTChar, LTFigure, LTPage

# To extract text from tables in PDF
import pdfplumber

# To extract the images from the PDFs
from pdf2image import convert_from_path

# To perform OCR to extract text from images
from file_operations.image import image2str


def _text_extraction(element: LTTextContainer) -> tuple[str, list]:
    """Extract text.

    Args:
        element (LTTextContainer): element

    Returns:
        tuple[str, list]: text extracted (line_text, format_per_line)
    """

    # Extracting the text from the in line text element
    line_text = element.get_text()

    # Find the formats of the text
    # Initialize the list with all the formats appeared in the line of text
    line_formats = []
    for text_line in element:
        if isinstance(text_line, LTTextContainer):
            # Iterating through each character in the line of text
            for character in text_line:
                if isinstance(character, LTChar):
                    # Append the font name of the character
                    line_formats.append(character.fontname)
                    # Append the font size of the character
                    line_formats.append(character.size)
    # Find the unique font sizes and names in the line
    format_per_line = list(set(line_formats))

    # Return a tuple with the text in each line along with its format
    return (line_text, format_per_line)


def _extract_table(pdf_path: str, page_num: int, table_num: int) -> Any:
    """Extract tables from the page.

    Args:
        pdf_path (str): path to pdf file
        page_num (int): page number
        table_num (int): table number

    Returns:
        Any: _description_
    """

    # Open the pdf file
    pdf = pdfplumber.open(pdf_path)
    # Find the examined page
    table_page = pdf.pages[page_num]
    # Extract the appropriate table
    table = table_page.extract_tables()[table_num]

    return table


def _table_converter(table: Any) -> str:
    """Convert table into appropriate format.

    Args:
        table (Any): table

    Returns:
        str: table string
    """

    table_string = ""
    # Iterate through each row of the table
    for row in table:
        # Remove the line breaker from the wrapted texts
        cleaned_row = [
            (
                item.replace("\n", " ")
                if item is not None and "\n" in item
                else "None" if item is None else item
            )
            for item in row
        ]
        # Convert the table into a string
        table_string += "|" + "|".join(cleaned_row) + "|" + "\n"
    # Removing the last line break
    table_string = table_string[:-1]
    return table_string


def _is_element_inside_any_table(
    element: LTComponent, page: LTPage, tables: list
) -> bool:
    """Check if the element is in any tables present in the page.

    Args:
        element (LTComponent): element
        page (LTPage): page
        tables (list): tables

    Returns:
        bool: element is in any tables present in the page
    """

    x0, y0up, x1, y1up = element.bbox
    # Change the cordinates because the pdfminer counts from the botton to top of the page
    y0 = page.bbox[3] - y1up
    y1 = page.bbox[3] - y0up
    for table in tables:
        tx0, ty0, tx1, ty1 = table.bbox
        if tx0 <= x0 <= x1 <= tx1 and ty0 <= y0 <= y1 <= ty1:
            return True
    return False


def _find_table_for_element(element: LTComponent, page: LTPage, tables: list) -> int:
    """Find the table for a given element

    Args:
        element (LTComponent): element
        page (LTPage): page
        tables (list): tables

    Returns:
        int: index of the table
    """

    x0, y0up, x1, y1up = element.bbox
    # Change the cordinates because the pdfminer counts from the botton to top of the page
    y0 = page.bbox[3] - y1up
    y1 = page.bbox[3] - y0up
    for i, table in enumerate(tables):
        tx0, ty0, tx1, ty1 = table.bbox
        if tx0 <= x0 <= x1 <= tx1 and ty0 <= y0 <= y1 <= ty1:
            return i  # Return the index of the table
    return None


def _crop_image(element: LTComponent, page_obj: PyPDF2.PdfReader) -> None:
    """Crop the image elements from PDFs

    Args:
        element (LTComponent): element
        page_obj (PyPDF2.PdfReader): page
    """
    # Get the coordinates to crop the image from PDF
    [image_left, image_top, image_right, image_bottom] = [
        element.x0,
        element.y0,
        element.x1,
        element.y1,
    ]
    # Crop the page using coordinates (left, bottom, right, top)
    page_obj.mediabox.lower_left = (image_left, image_bottom)
    page_obj.mediabox.upper_right = (image_right, image_top)
    # Save the cropped page to a new PDF
    cropped_pdf_writer = PyPDF2.PdfWriter()
    cropped_pdf_writer.add_page(page_obj)
    # Save the cropped PDF to a new file
    with open("cropped_image.pdf", "wb") as cropped_pdf_file:
        cropped_pdf_writer.write(cropped_pdf_file)


def _convert_to_images(input_file: str) -> None:
    """Convert the PDF to images

    Args:
        input_file (str): image file path
    """

    images = convert_from_path(
        input_file, poppler_path=r"C:\Program Files\poppler-23.11.0\Library\bin"
    )
    image = images[0]
    output_file = "PDF_image.png"
    image.save(output_file, "PNG")


def read_pdf(pdf_path: str) -> str:
    """Read PDF

    Args:
        pdf_path (str): pdf file path

    Returns:
        str: text from pdf
    """

    # Create a pdf file object
    pdf_file_obj = open(pdf_path, "rb")
    # Create a pdf reader object
    pdf_readed = PyPDF2.PdfReader(pdf_file_obj)

    # Create the dictionary to extract text from each image
    text_per_page = {}
    # Create a boolean variable for image detection
    image_flag = False

    # We extract the pages from the PDF
    for pagenum, page in enumerate(extract_pages(pdf_path)):
        # Initialize the variables needed for the text extraction from the page
        page_obj = pdf_readed.pages[pagenum]
        page_text = []
        line_format = []
        text_from_images = []
        text_from_tables = []
        page_content = []
        # Initialize the number of the examined tables
        table_in_page = -1
        # Open the pdf file
        pdf = pdfplumber.open(pdf_path)
        # Find the examined page
        page_tables = pdf.pages[pagenum]
        # Find the number of tables in the page
        tables = page_tables.find_tables()
        if len(tables) != 0:
            table_in_page = 0

        # Extracting the tables of the page
        for table_num in range(len(tables)):
            # Extract the information of the table
            table = _extract_table(pdf_path, pagenum, table_num)
            # Convert the table information in structured string format
            table_string = _table_converter(table)
            # Append the table string into a list
            text_from_tables.append(table_string)

        # Find all the elements
        page_elements = [(element.y1, element) for element in page._objs]
        # Sort all the element as they appear in the page
        page_elements.sort(key=lambda a: a[0], reverse=True)

        # Find the elements that composed a page
        for i, component in enumerate(page_elements):
            del i

            # Extract the element of the page layout
            element = component[1]

            # Check the elements for tables
            if table_in_page == -1:
                pass
            else:
                if _is_element_inside_any_table(element, page, tables):
                    table_found = _find_table_for_element(element, page, tables)
                    if table_found == table_in_page and table_found is not None:
                        page_content.append(text_from_tables[table_in_page])
                        page_text.append("table")
                        line_format.append("table")
                        table_in_page += 1
                    # Pass this iteration because the content of this element was extracted from
                    # the tables
                    continue

            if not _is_element_inside_any_table(element, page, tables):
                # Check if the element is text element
                if isinstance(element, LTTextContainer):
                    # Use the function to extract the text and format for each text element
                    (line_text, format_per_line) = _text_extraction(element)
                    # Append the text of each line to the page text
                    page_text.append(line_text)
                    # Append the format for each line containing text
                    line_format.append(format_per_line)
                    page_content.append(line_text)

                # Check the elements for images
                if isinstance(element, LTFigure):
                    # Crop the image from PDF
                    _crop_image(element, page_obj)
                    # Convert the croped pdf to image
                    _convert_to_images("cropped_image.pdf")
                    # Extract the text from image
                    image_text = image2str("PDF_image.png")
                    text_from_images.append(image_text)
                    page_content.append(image_text)
                    # Add a placeholder in the text and format lists
                    page_text.append("image")
                    line_format.append("image")
                    # Update the flag for image detection
                    image_flag = True

        # Create the key of the dictionary
        dctkey = "Page_" + str(pagenum)
        # Add the list of list as value of the page key
        text_per_page[dctkey] = [
            page_text,
            line_format,
            text_from_images,
            text_from_tables,
            page_content,
        ]

    # Close the pdf file object
    pdf_file_obj.close()

    # Delete the additional files created if image is detected
    if image_flag:
        os.remove("cropped_image.pdf")
        os.remove("PDF_image.png")

    # Display the content of the page
    result = str()
    for key, item in text_per_page.items():
        del key
        result += "".join(item[4])
    return result
