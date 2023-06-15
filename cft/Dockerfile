FROM python:3.11.3

RUN mkdir /exapp

WORKDIR /exapp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ls && gunicorn api:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
EXPOSE 8000