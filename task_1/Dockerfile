FROM python:3.9
# Make work directory
RUN mkdir /app
WORKDIR /app
ADD . /app
# Install requirements
RUN pip install -r requirements.txt
CMD ["python","./main.py"]