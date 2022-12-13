import fitz

# FOLDERS
INPUTS_FOLDER = r'invoices/0_RAW'
TEMP_FOLDER = r'invoices/1_TO DO OCR'  # FOR PDFs CONVERTED TO JPGs
REPORTS_FOLDER = r'invoices/2_REPORTS'

# PDF TO IMAGE
DPI = 300  # choose desired dpi here
ZOOM = DPI / 72  # zoom factor, standard: 72 dpi
MAGNIFY = fitz.Matrix(ZOOM, ZOOM)  # magnifies in x, resp. y direction

# FLAG TO PREPROCESS IMAGE BEFORE TESSERACT
IMAGE_PREPROCESSING = False

# REGULAR EXPRESSIONS TO EXTRACT DATA FROM AN INVOICE
REGEXP_INV_NUMBER = r'#\d+'
REGEXP_INV_DATE = r'\d{2}\/\d{2}\/\d{4}'