FROM python:3.7-slim 
WORKDIR /app
RUN ["ls"]
COPY api_yamdb/requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
RUN ["ls"]
COPY . . 
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
