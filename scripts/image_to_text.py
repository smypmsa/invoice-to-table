import cv2
import pytesseract
import re

from config import IMAGE_PREPROCESSING, REGEXP_INV_NUMBER, REGEXP_INV_DATE


# Get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# Thresholding
def do_thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# Combination of preprocessing steps
def do_combined_preprocessing(image):
        disnoised_img = remove_noise(image)
        grayed_img = get_grayscale(disnoised_img)
        threshed_img = do_thresholding(grayed_img)

        return threshed_img


def process_invoice(filename: str, file_path: str):
    """
    Process an invoice image with the help of Tesseract OCR and
    returns its number and date.

    :param
    filename: A file name
    file_path: A path to an invoice image
    :return:
    inv_data (dict): An invoice file name, invoice number and date
    """

    img = cv2.imread(file_path)

    # Crop image (client's invoices have a standard format,
    # so we can crop unnecessary part)

    cropped_height = int(img.shape[0] * 1/5)
    cropped_width = int(img.shape[1] * 2/3)
    cropped_img = img[:cropped_height, cropped_width:]

    if IMAGE_PREPROCESSING:
        cropped_img = do_combined_preprocessing(cropped_img)

    # Run the tesseract engine
    recognized_text = pytesseract.image_to_string(cropped_img, lang='eng')

    inv_number = re.findall(REGEXP_INV_NUMBER, recognized_text, re.MULTILINE)[0]
    inv_date = re.findall(REGEXP_INV_DATE, recognized_text, re.MULTILINE)[0]

    inv_data = {'File name': filename,
                'Invoice number': inv_number,
                'Invoice date': inv_date}

    return inv_data
