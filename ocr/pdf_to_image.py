import fitz

from config import MAGNIFY


def convert_pdf_to_image(contents):
    pdf_file = fitz.open(stream=contents, filetype="pdf")

    for page in pdf_file:
        img = page.get_pixmap(matrix=MAGNIFY)  # render only the first page to an image
        img_bytes = img.tobytes()

        return img_bytes
