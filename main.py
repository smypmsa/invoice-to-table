from fastapi import FastAPI, File, UploadFile
from typing import List
from fastapi.responses import FileResponse

from config import INPUTS_FOLDER, TEMP_FOLDER, REPORTS_FOLDER

from scripts.pdf_to_image import convert_pdf_to_image
from scripts.image_to_text import process_invoice
from scripts.helpers import clean_folders

import csv

import uvicorn


app = FastAPI()


@app.post("/upload_invoices")
def upload_invoices(files: List[UploadFile] = File(...)):

    # Clean folders in order not to process any previous files
    clean_folders(INPUTS_FOLDER, TEMP_FOLDER, REPORTS_FOLDER)

    # Arrays for storing the results of processing
    header = ['File name', 'Invoice number', 'Invoice date']
    report = []

    # Process files
    for file in files:
        try:
            contents = file.file.read()
            uploaded_file_path = f'{INPUTS_FOLDER}/{file.filename}'

            with open(uploaded_file_path, 'wb') as f:
                f.write(contents)

            pdf_converted_to_image_path = convert_pdf_to_image(uploaded_file_path)
            invoice_data = process_invoice(file.filename, pdf_converted_to_image_path)
            report.append(invoice_data)

        except Exception as error:
            report.append({'File name': file.filename,
                           'Invoice number': error,
                           'Invoice date': 'Error while processing a file'})
        finally:
            print('Success!')

    # Write the results to a csv file
    report_path = f'{REPORTS_FOLDER}/report.csv'
    with open(report_path, 'w', newline='') as report_file:
        dict_writer = csv.DictWriter(report_file, header)
        dict_writer.writeheader()
        dict_writer.writerows(report)

    clean_folders(INPUTS_FOLDER, TEMP_FOLDER)

    return FileResponse(report_path)
