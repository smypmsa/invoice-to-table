FROM python:3.9

RUN mkdir /project_invoices

WORKDIR /project_invoices

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update && apt-get install tesseract-ocr -y

COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8001"]