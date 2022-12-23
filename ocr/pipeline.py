import base64

from ocr_tasks.pdf_to_image import convert_pdf_to_image
from ocr_tasks.image_to_text import do_image_ocr


def process_pdf_invoice(filename: str, pdf_bytes_str: str):
    pdf_bytes = base64.b64decode(pdf_bytes_str)
    img_bytes = convert_pdf_to_image(pdf_bytes)
    invoice_data = do_image_ocr(filename, img_bytes)

    return invoice_data
