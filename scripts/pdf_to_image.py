import fitz
import glob

from config import INPUTS_FOLDER, TEMP_FOLDER, MAGNIFY


def convert_pdf_to_image(pdf_path):
    pdf_file = fitz.open(pdf_path)
    output_path = f"{TEMP_FOLDER}/{pdf_path.split('/')[-1]}.jpg"

    for page in pdf_file:
        img = page.get_pixmap(matrix=MAGNIFY)  # render page to an image
        img.save(output_path)
        break

    return output_path
