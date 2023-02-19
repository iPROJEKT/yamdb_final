FROM python:3.7-slim 
WORKDIR /app
<<<<<<< HEAD
COPY requirements.txt . 
RUN pip3 install -r requirements.txt --no-cache-dir 
=======
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
>>>>>>> fc8dc6a547f038f887249ceef647df43ec7ea788
COPY . . 
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
