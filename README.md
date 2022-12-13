# Invoice to table
FastAPI + Tesseract OCR. Easy to use API to process invoices with Tesseract OCR. Send invoices in PDF, get the CSV table with extracted data (invoice number and date).


### Docker

#### Create a docker image
`docker image build --tag invoices_app .`

#### Start a docker container
`docker container run --publish 8001:80 --name invoices_app_container invoices_app`


### Terminal
#### Start server manually
`uvicorn main:app --host 0.0.0.0 --port 8001`
